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
        return cls.get_first_by_filter(name=name)

    @classmethod
    def add_teacher(cls, school, teacher):
        school.teachers.append(teacher)
        cls._session.commit()
        return school

    @classmethod
    def add_preceptor(cls, school, preceptor):
        school.preceptors.append(preceptor)
        cls._session.commit()
        return school

    @classmethod
    def add_student(cls, school, student):
        school.students.append(student)
        cls._session.commit()
        return school

    @classmethod
    def add_course(cls, school, course):
        school.courses.append(course)
        cls._session.commit()
        return school

    @classmethod
    def get_courses(cls, school):
        return school.courses

    @classmethod
    def get_students(cls, school):
        return school.students

    @classmethod
    def get_teachers(cls, school):
        return school.teachers

    @classmethod
    def get_preceptors(cls, school):
        return school.preceptors


class TeacherService(GenericService):
    _model = Teacher

    @classmethod
    def get_by_name(cls, name: str):
        return cls.get_first_by_filter(name=name)

    @classmethod
    def get_by_specialty(cls, specialty: str):
        return cls.get_all_by_filter(specialty=specialty)

    @classmethod
    def get_by_school(cls, school):
        return cls.get_all_by_filter(school_id=school.id)


class PreceptorService(GenericService):
    _model = Preceptor

    @classmethod
    def get_by_name(cls, name: str):
        return cls.get_first_by_filter(name=name)

    @classmethod
    def get_by_school(cls, school):
        return cls.get_all_by_filter(school_id=school.id)


class ClassroomService(GenericService):
    _model = Classroom

    @classmethod
    def get_by_name(cls, name: str):
        return cls.get_first_by_filter(name=name)

    @classmethod
    def get_students(cls, classroom):
        return classroom.students

    @classmethod
    def add_student(cls, classroom, student):
        classroom.students.append(student)
        cls._session.commit()
        return classroom

    @classmethod
    def remove_student(cls, classroom, student):
        classroom.students.remove(student)
        cls._session.commit()
        return classroom

    @classmethod
    def get_courses(cls, classroom):
        return classroom.courses

    @classmethod
    def add_course(cls, classroom, course):
        classroom.courses.append(course)
        cls._session.commit()
        return classroom


class CourseService(GenericService):
    _model = Course

    @classmethod
    def get_by_name(cls, name: str):
        return cls.get_first_by_filter(name=name)

    @classmethod
    def get_by_teacher(cls, teacher: Teacher):
        return cls.get_all_by_filter(teacher_id=teacher.id)

    @classmethod
    def get_by_preceptor(cls, preceptor: Preceptor):
        return cls.get_all_by_filter(preceptor_id=preceptor.id)

    @classmethod
    def get_by_school(cls, school: School):
        return cls.get_all_by_filter(school_id=school.id)

    @classmethod
    def get_students(cls, course: Course):
        return course.students

    @classmethod
    def add_student(cls, course: Course, student: Student):
        course.students.append(student)
        cls._session.commit()
        return course

    @classmethod
    def remove_student(cls, course: Course, student: Student):
        course.students.remove(student)
        cls._session.commit()
        return course

    @classmethod
    def get_classroom(cls, course: Course):
        return course.classroom

    @classmethod
    def add_classroom(cls, course: Course, classroom: Classroom):
        course.classroom = classroom
        cls._session.commit()
        return course

    @classmethod
    def add_teacher(cls, course: Course, teacher: Teacher):
        course.teacher = teacher
        cls._session.commit()
        return course

    @classmethod
    def add_preceptor(cls, course: Course, preceptor: Preceptor):
        course.preceptor = preceptor
        cls._session.commit()
        return course


class StudentService(GenericService):
    _model = Student

    @classmethod
    def get_by_name(cls, name: str):
        return cls.get_first_by_filter(name=name)

    @classmethod
    def get_by_email(cls, email: str):
        return cls.get_first_by_filter(email=email)

    @classmethod
    def get_by_document(cls, document: str):
        return cls.get_first_by_filter(document=document)

    @classmethod
    def get_by_nationality(cls, nationality: str):
        return cls.get_all_by_filter(nationality=nationality)
