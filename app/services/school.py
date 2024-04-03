from typing import List

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import joinedload

from app.blueprints.exceptions import APIException
from app.blueprints.exceptions import FilterException
from app.blueprints.exceptions import NotFoundException
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

    @classmethod
    def _get_attendance_by_date(cls, course, date_attendance: str):
        attendance = next(
            (att for att in course.attendances if att.date == date_attendance), None
        )
        if not attendance:
            raise NotFoundException(
                f"No attendance record found for course on date {date_attendance}"
            )
        return attendance

    @classmethod
    def get_by_id_and_date_attendance(cls, course_id: str, date_attendance: str):
        try:
            course = (
                cls._session.query(Course)
                .options(
                    joinedload(Course.attendances).joinedload(
                        Attendance.attendance_details
                    )
                )
                .filter(Course.id == course_id)
                .one_or_none()
            )
            if not course:
                raise NotFoundException("Course not found")
            total_students_enrolled = len(course.students)
            # Ya que la fecha siempre está presente, busca directamente la asistencia correspondiente
            attendance = cls._get_attendance_by_date(course, date_attendance)
            total_present = sum(
                detail.is_present for detail in attendance.attendance_details
            )
            total_absentees = sum(
                not detail.is_present for detail in attendance.attendance_details
            )

            return {
                "course": course,
                "attendance": attendance,
                "total_students_enrolled": total_students_enrolled,
                "total_students_present": total_present,
                "total_students_absent": total_absentees,
            }
        except SQLAlchemyError as e:
            raise FilterException(f"Error in filter operation: {str(e)}")


class StudentService(GenericService):
    _model = Student

    @classmethod
    def get_by_name(cls, name: str):
        try:
            return cls._session.query(cls._model).filter_by(name=name).first()
        except SQLAlchemyError as e:
            raise FilterException(f"Error in filter operation: {str(e)}")

    @classmethod
    def check_if_student_is_active(cls, student_id: str):
        try:
            student = cls.get_by_id(student_id)
            return student.is_active
        except SQLAlchemyError as e:
            raise FilterException(f"Error in filter operation: {str(e)}")

    @classmethod
    def disable_student(cls, student_id: str):
        try:
            student = cls.get_by_id(student_id)
            student.is_active = False
            cls._session.commit()
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
    student_service = StudentService

    @classmethod
    def get_by_date(cls, date: str):
        try:
            return cls._session.query(cls._model).filter_by(date=date).first()
        except SQLAlchemyError as e:
            raise FilterException(f"Error in filter operation: {str(e)}")

    @classmethod
    def create_attendance_and_detail(cls, attendance_data: dict):
        student_attendance_list = attendance_data.pop("students")
        attendance = cls.create(**attendance_data)
        cls.add_list_students_to_attendance(attendance, student_attendance_list)
        return attendance

    @classmethod
    def add_list_students_to_attendance(
        cls, attendance: Attendance, student_attendance_list: List[dict]
    ):
        for student_attendance in student_attendance_list:
            if cls.student_service.check_if_student_is_active(
                student_attendance["student_id"]
            ):
                attendance_detail = AttendanceDetail(
                    attendance_id=attendance.id,
                    student_id=student_attendance["student_id"],
                    is_present=student_attendance["is_present"],
                    absence_reason=student_attendance.get("reason_absence"),
                )
                cls._session.add(attendance_detail)
        cls._session.commit()
        return attendance

    @classmethod
    def update_attendance_and_details(cls, attendance_id: str, attendance_data: dict):
        student_attendance_list = attendance_data.pop("students")
        try:
            attendance_updated = cls.update(attendance_id, **attendance_data)
            cls._update_attendance_details(attendance_updated, student_attendance_list)
            return attendance_updated
        except SQLAlchemyError as e:
            raise FilterException(f"Error in update operation: {str(e)}")

    @classmethod
    def _update_attendance_details(
        cls, attendance: Attendance, student_attendance_list: List[dict]
    ):
        for student_attendance in student_attendance_list:
            student_id = student_attendance["student_id"]
            attendance_detail = (
                cls._session.query(AttendanceDetail)
                .filter_by(attendance_id=attendance.id, student_id=student_id)
                .one_or_none()
            )

            if attendance_detail:
                attendance_detail.is_present = student_attendance["is_present"]
                attendance_detail.absence_reason = student_attendance.get(
                    "reason_absence"
                )
            else:
                if cls.student_service.check_if_student_is_active(student_id):
                    new_attendance_detail = AttendanceDetail(
                        attendance_id=attendance.id,
                        student_id=student_id,
                        is_present=student_attendance["is_present"],
                        absence_reason=student_attendance.get("reason_absence"),
                    )
                    cls._session.add(new_attendance_detail)
        cls._session.commit()
