import json
from datetime import date

from fastapi import FastAPI, UploadFile, HTTPException, status, File, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from tortoise.contrib.fastapi import register_tortoise
from tortoise.exceptions import DoesNotExist

from app.database import TORTOISE_ORM
from app.schemas import Tariff
from app.utils import (
    get_cargo,
    get_rate_by_cargo_id,
    create_object_from_dict
)

app = FastAPI()


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={"detail": "The json data is incorrect"}
    )


@app.post("/tariff")
async def tariff_upload(tariff: Tariff):
    tariff = json.loads(tariff.json())
    await create_object_from_dict(tariff=tariff)
            
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
    await create_object_from_dict(tariff=tariff)

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