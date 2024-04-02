from marshmallow import fields
from marshmallow import Schema


class AuthSchema(Schema):
    email = fields.Email(required=True)
    password = fields.Str(required=True)
