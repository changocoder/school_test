from sqlalchemy.exc import SQLAlchemyError

from app.blueprints.exceptions import APIException
from app.blueprints.exceptions import FilterException
from app.models.school import Attendance
from app.models.school import AttendanceDetail
from app.models.school import Classroom
from app.models.school import Course
from app.models.school import Preceptor
from app.models.school import School
from app.models.school import Student
from app.models.school import Teacher
from app.services.base import GenericService


class SchoolService(GenericService):
    _model = School

    @classmethod
    def get_by_name(cls, name: str):
        try:
            return cls._session.query(cls._model).filter_by(name=name).first()
        except SQLAlchemyError as e:
            raise FilterException(f"Error in filter operation: {str(e)}")

    @classmethod
    def add_teacher(cls, school, teacher):
        school.teachers.append(teacher)
        cls._session.commit()
        return school

    @classmethod
    def add_student(cls, school, student):
        school.students.append(student)
        cls._session.commit()
        return school

    @classmethod
    def add_preceptor(cls, school, preceptor):
        school.preceptors.append(preceptor)
        cls._session.commit()
        return school

    @classmethod
    def add_course(cls, school, course):
        school.courses.append(course)
        cls._session.commit()
        return school

    @classmethod
    def add_classroom(cls, school, classroom):
        # implment try except
        school.classrooms.append(classroom)
        cls._session.commit()
        return school


class TeacherService(GenericService):
    _model = Teacher

    @classmethod
    def get_by_specialty(cls, specialty: str):
        try:
            return cls._session.query(cls._model).filter_by(specialty=specialty).first()
        except SQLAlchemyError as e:
            raise FilterException(f"Error in filter operation: {str(e)}")


class PreceptorService(GenericService):
    _model = Preceptor

    @classmethod
    def get_by_name(cls, name: str):
        try:
            return cls._session.query(cls._model).filter_by(name=name).first()
        except SQLAlchemyError as e:
            raise FilterException(f"Error in filter operation: {str(e)}")


class ClassroomService(GenericService):
    _model = Classroom

    @classmethod
    def get_by_name(cls, name: str):
        try:
            return cls._session.query(cls._model).filter_by(name=name).first()
        except SQLAlchemyError as e:
            raise FilterException(f"Error in filter operation: {str(e)}")


class CourseService(GenericService):
    _model = Course

    @classmethod
    def get_by_name(cls, name: str):
        try:
            return cls._session.query(cls._model).filter_by(name=name).first()
        except SQLAlchemyError as e:
            raise FilterException(f"Error in filter operation: {str(e)}")

    @classmethod
    def enroll_student(cls, data_enroll: dict):
        course = cls.get_by_id(data_enroll["course_id"])
        student = StudentService.get_by_id(data_enroll["student_id"])

        if cls.check_if_student_is_enrolled(course, student):
            raise APIException("Student already enrolled in this course", 400)

        if not cls.check_if_student_and_course_are_the_same_school(course, student):
            raise APIException("Student and course are not from the same school", 400)

        try:
            course.students.append(student)
            cls._session.commit()
        except SQLAlchemyError as e:
            raise APIException(f"Error enrolling student: {str(e)}", 400)

    @classmethod
    def check_if_student_is_enrolled(cls, course: Course, student: Student):
        return student in course.students

    @classmethod
    def check_if_student_and_course_are_the_same_school(
        cls, course: Course, student: Student
    ):
        return course.school == student.school


class StudentService(GenericService):
    _model = Student

    @classmethod
    def get_by_name(cls, name: str):
        try:
            return cls._session.query(cls._model).filter_by(name=name).first()
        except SQLAlchemyError as e:
            raise FilterException(f"Error in filter operation: {str(e)}")


class AttendanceDetailService(GenericService):
    _model = AttendanceDetail

    @classmethod
    def get_by_attendance_id(cls, attendance_id: str):
        try:
            return (
                cls._session.query(cls._model)
                .filter_by(attendance_id=attendance_id)
                .all()
            )
        except SQLAlchemyError as e:
            raise FilterException(f"Error in filter operation: {str(e)}")

    @classmethod
    def get_by_student_id(cls, student_id: str):
        try:
            return cls._session.query(cls._model).filter_by(student_id=student_id).all()
        except SQLAlchemyError as e:
            raise FilterException(f"Error in filter operation: {str(e)}")

    @classmethod
    def get_by_attendance_and_student_id(cls, attendance_id: str, student_id: str):
        try:
            return (
                cls._session.query(cls._model)
                .filter_by(attendance_id=attendance_id, student_id=student_id)
                .first()
            )
        except SQLAlchemyError as e:
            raise FilterException(f"Error in filter operation: {str(e)}")


class AttendanceService(GenericService):
    _model = Attendance

    @classmethod
    def get_by_date(cls, date: str):
        try:
            return cls._session.query(cls._model).filter_by(date=date).first()
        except SQLAlchemyError as e:
            raise FilterException(f"Error in filter operation: {str(e)}")
