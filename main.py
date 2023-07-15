import json
from iso8601.iso8601 import ParseError
from datetime import date

from fastapi import FastAPI, UploadFile, HTTPException, status, File
from tortoise.contrib.fastapi import register_tortoise
from tortoise.exceptions import DoesNotExist

from app.database import TORTOISE_ORM
from app.models import CargoIn_Pydantic, RateIn_Pydantic
from app.utils import (
    create_cargo, 
    create_rate,
    get_cargo,
    get_rate,
    get_rate_by_cargo_id
)

app = FastAPI()



@app.post("/tariff")
async def tariff_upload(tariff: dict):
    try:
        for key, values in tariff.items():
            for value in values:
                try:
                    cargo = await get_cargo(value["cargo_type"])
                except DoesNotExist:
                    cargoIn = CargoIn_Pydantic(cargo_type=value["cargo_type"])
                    cargo = await create_cargo(cargo=cargoIn)
                try:
                    rate = await get_rate(date=key, rate=value["rate"])
                except DoesNotExist:
                    rate = RateIn_Pydantic(date=key, rate=value["rate"])
                    await create_rate(rate=rate, cargo_id=cargo.id)
    except (TypeError, KeyError, ParseError):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The json data is incorrect"
        )
            
    return tariff

@app.post("/tariff/upload_file")
async def tariff_file_upload(file: UploadFile = File()):
    if file.content_type != "application/json":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Upload json file"
        )

    contents = await file.read()
    contents = contents.decode("utf-8")
    tariff = json.loads(contents) 

    try:
        for key, values in tariff.items():
            for value in values:
                try:
                    cargo = await get_cargo(value["cargo_type"])
                except DoesNotExist:
                    cargoIn = CargoIn_Pydantic(cargo_type=value["cargo_type"])
                    cargo = await create_cargo(cargo=cargoIn)
                try:
                    rate = await get_rate(date=key, rate=value["rate"])
                except DoesNotExist:
                    rate = RateIn_Pydantic(date=key, rate=value["rate"])
                    await create_rate(rate=rate, cargo_id=cargo.id)
    except (TypeError, KeyError, ParseError):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The data in the json file is incorrect"
        )

    return tariff


@app.get("/cost_insurance")
async def get_cost_of_insurance(declared_cost: float, cargo_type: str, date: date):
    try:
        cargo_type = await get_cargo(cargo_type=cargo_type)
        rate = await get_rate_by_cargo_id(date=date, cargo_type_id=cargo_type.id)
    except DoesNotExist as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"{exc}"
        )
    
    cost_of_insurance = rate.rate * declared_cost

    return {"cost_of_insurance": cost_of_insurance}



register_tortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas=True,
    add_exception_handlers=True,
)