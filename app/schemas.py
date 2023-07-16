from pydantic import BaseModel, constr


pattern = r'(?<!\d)\d{4}-(?:0?[1-9]|1[0-2])-(?:0?[1-9]|[12][0-9]|3[01])(?!\d)'
Date = constr(regex=pattern)


class MyModel(BaseModel):
    class Config:
        allow_population_by_field_name = True


class Data(MyModel):
    cargo_type: str
    rate: float


class Tariff(MyModel):
    __root__: dict[Date, list[Data]]