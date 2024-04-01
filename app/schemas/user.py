from marshmallow import Schema, fields


class UserSchema(Schema):
    id = fields.Str()
    name = fields.Str()
    last_name = fields.Str()
    email = fields.Str()