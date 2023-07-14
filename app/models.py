from tortoise.models import Model
from tortoise import fields


class Cargo(Model):
    id = fields.IntField(pk=True)
    cargo_type = fields.CharField(max_length=255, unique=True)


class Rate(Model):
    id = fields.IntField(pk=True)
    date = fields.DateField(null=False)
    rate = fields.FloatField(null=False)
    cargo_type = fields.ForeignKeyField('cargo.Cargo', related_name='rates')