from marshmallow import fields
from marshmallow import Schema
from marshmallow import ValidationError


class UserSchema(Schema):
    name = fields.Str()
    last_name = fields.Str()
    email = fields.Email()
    password = fields.Str()
    password_confirmation = fields.Str()

    def validate_password(self, data):
        if data["password"] != data["password_confirmation"]:
            raise ValidationError("Passwords must match")
        return data
