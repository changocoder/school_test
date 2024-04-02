from marshmallow import fields
from marshmallow import Schema


class SchoolSchema(Schema):
    id = fields.UUID(dump_only=True)
    name = fields.String(required=True)
    address = fields.String(required=True)
    phone = fields.String(required=False)
