from marshmallow import EXCLUDE
from marshmallow import fields
from marshmallow import Schema


class SchoolSchema(Schema):
    id = fields.UUID(dump_only=True)
    name = fields.String(required=True)
    address = fields.String(required=True)
    phone = fields.String(required=False)


class TeacherSchema(Schema):
    id = fields.UUID(dump_only=True)
    name = fields.String(required=True)
    last_name = fields.String(required=True)
    document = fields.String(required=True)
    specialty = fields.String(required=True)
    school_id = fields.UUID(required=True)

    class Meta:
        unknown = EXCLUDE


class PreceptorSchema(Schema):
    id = fields.UUID(dump_only=True)
    name = fields.String(required=True)
    last_name = fields.String(required=True)
    document = fields.String(required=True)
    school_id = fields.UUID(required=True)

    class Meta:
        unknown = EXCLUDE


class ClassroomSchema(Schema):
    id = fields.UUID(dump_only=True)
    name = fields.String(required=True)

    class Meta:
        unknown = EXCLUDE


class CourseSchema(Schema):
    id = fields.UUID(dump_only=True)
    name = fields.String(required=True)
    school_id = fields.UUID(required=True)
    teacher_id = fields.UUID(required=True)
    preceptor_id = fields.UUID(required=True)

    class Meta:
        unknown = EXCLUDE
