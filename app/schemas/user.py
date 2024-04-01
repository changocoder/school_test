from marshmallow import fields
from marshmallow import Schema


class UserSchema(Schema):
    id = fields.Str()
    name = fields.Str()
    last_name = fields.Str()
    email = fields.Str()
