from sqlalchemy.exc import SQLAlchemyError

from app.blueprints.exceptions import FilterException
from app.models.school import School
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
