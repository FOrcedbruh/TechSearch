from tortoise import Model, fields


class BaseModel(Model):
    id = fields.BigIntField(primary_key=True)

    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
