from datetime import date

from app.models import (
    Cargo, 
    Rate, 
    CargoIn_Pydantic, 
    Cargo_Pydantic, 
    RateIn_Pydantic, 
    Rate_Pydantic
)


async def create_cargo(cargo: CargoIn_Pydantic):
    cargo = await Cargo.create(**cargo.dict())
    return await Cargo_Pydantic.from_tortoise_orm(cargo)

async def get_cargo(cargo_type: str):
    return await Cargo_Pydantic.from_queryset_single(Cargo.get(cargo_type=cargo_type))

async def create_rate(rate: RateIn_Pydantic, cargo_id: int):
    rate = await Rate.create(**rate.dict(), cargo_type_id=cargo_id)
    return await Rate_Pydantic.from_tortoise_orm(rate)

async def get_rate(date: date, rate: float):
    return await Rate_Pydantic.from_queryset_single(Rate.get(date=date, rate=rate))

async def get_rate_by_cargo_id(date: date, cargo_type_id: int):
    return await Rate_Pydantic.from_queryset_single(Rate.get(date=date, cargo_type_id=cargo_type_id))