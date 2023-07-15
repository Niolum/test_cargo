from tortoise.models import Model
from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator


class Cargo(Model):
    id = fields.IntField(pk=True)
    cargo_type = fields.CharField(max_length=255, unique=True)

    class PydanticMeta:
        pass


class Rate(Model):
    id = fields.IntField(pk=True)
    date = fields.DateField(null=False)
    rate = fields.FloatField(null=False)
    cargo_type = fields.ForeignKeyField('cargo.Cargo', related_name='rates')

    class PydanticMeta:
        pass


Cargo_Pydantic = pydantic_model_creator(Cargo, name="Cargo")
CargoIn_Pydantic = pydantic_model_creator(Cargo, name="CargoIn", exclude_readonly=True)
Rate_Pydantic = pydantic_model_creator(Rate, name="Rate")
RateIn_Pydantic = pydantic_model_creator(Rate, name="RateIn", exclude_readonly=True)