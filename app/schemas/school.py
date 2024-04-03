from marshmallow import EXCLUDE
from marshmallow import fields
from marshmallow import Schema
from marshmallow import validates
from marshmallow import ValidationError

from app.models.enums import AbsenceReasonEnum


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

    class Meta:
        unknown = EXCLUDE


class PreceptorSchema(Schema):
    id = fields.UUID(dump_only=True)
    name = fields.String(required=True)
    last_name = fields.String(required=True)
    document = fields.String(required=True)

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


class StudentSchema(Schema):
    id = fields.UUID(dump_only=True)
    name = fields.String(required=True)
    last_name = fields.String(required=True)
    document = fields.String(required=True)
    email = fields.String(required=True)
    nationality = fields.String(required=True)
    school_id = fields.UUID(required=True)

    class Meta:
        unknown = EXCLUDE


class EnrollStudentSchema(Schema):
    student_id = fields.UUID(required=True)
    course_id = fields.UUID(required=True)

    class Meta:
        unknown = EXCLUDE


class StudentAttendanceSchema(Schema):
    student_id = fields.UUID(required=True)
    is_present = fields.Boolean(required=True)
    reason_absence = fields.Enum(AbsenceReasonEnum, required=False)

    class Meta:
        unknown = EXCLUDE

    @validates("reason_absence")
    def validate_reason_absence(self, value):
        if value is None:
            return

        if value not in [reason.value for reason in AbsenceReasonEnum]:
            raise ValidationError("Invalid absence reason")


class AttendanceDetailSchema(Schema):
    id = fields.UUID(dump_only=True)
    date = fields.Date(required=True)
    course_id = fields.UUID(required=True)
    students = fields.List(fields.Nested(StudentAttendanceSchema))

    class Meta:
        unknown = EXCLUDE

    @validates("students")
    def validate_students(self, value):
        if not value:
            raise ValidationError("Students list cannot be empty")

        students_ids = [student["student_id"] for student in value]
        if len(students_ids) != len(set(students_ids)):
            raise ValidationError("Duplicated students in list")
