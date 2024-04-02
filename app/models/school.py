from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import Date
from sqlalchemy import Enum
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import UUID
from sqlalchemy.orm import relationship

from app.models.db import Base
from app.models.enums import AbsenceReasonEnum


class Person(Base):
    __abstract__ = True
    name = Column(String)
    last_name = Column(String)
    document = Column(String, unique=True)


class School(Base):
    __tablename__ = "schools"

    name = Column(String)
    address = Column(String)
    phone = Column(String)

    teachers = relationship("Teacher", back_populates="school")
    preceptors = relationship("Preceptor", back_populates="school")
    students = relationship("Student", back_populates="school")
    courses = relationship("Course", back_populates="school")


class Teacher(Person):
    __tablename__ = "teachers"
    specialty = Column(String)
    school_id = Column(UUID(as_uuid=True), ForeignKey("schools.id"))
    school = relationship("School", back_populates="teachers")
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=True)
    user = relationship("User")
    # Más atributos y relaciones si son necesarios


class Preceptor(Person):
    __tablename__ = "preceptors"
    school_id = Column(UUID(as_uuid=True), ForeignKey("schools.id"))
    school = relationship("School", back_populates="preceptors")
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=True)
    user = relationship("User")
    # Atributos específicos del Preceptor


class Classroom(Base):
    __tablename__ = "classrooms"
    name = Column(String)
    students = relationship("Student", back_populates="classroom")


class Course(Base):
    __tablename__ = "courses"
    name = Column(String)
    school_id = Column(UUID(as_uuid=True), ForeignKey("schools.id"))
    school = relationship("School", back_populates="courses")
    teacher_id = Column(UUID(as_uuid=True), ForeignKey("teachers.id"))
    teacher = relationship("Teacher")
    preceptor_id = Column(UUID(as_uuid=True), ForeignKey("preceptors.id"))
    preceptor = relationship("Preceptor")
    students = relationship("Student", back_populates="course")


class Student(Person):
    __tablename__ = "students"
    email = Column(String, unique=True)
    nationality = Column(String)
    is_active = Column(Boolean, default=True)
    school_id = Column(UUID(as_uuid=True), ForeignKey("schools.id"))
    school = relationship("School", back_populates="students")
    classroom_id = Column(
        UUID(as_uuid=True), ForeignKey("classrooms.id"), nullable=True
    )
    classroom = relationship("Classroom", back_populates="students")
    course_id = Column(UUID(as_uuid=True), ForeignKey("courses.id"), nullable=True)
    course = relationship("Course", back_populates="students")
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=True)
    user = relationship("User")


class AttendanceDetail(Base):
    __tablename__ = "attendance_details"
    attendance_id = Column(
        UUID(as_uuid=True), ForeignKey("attendances.id"), primary_key=True
    )
    student_id = Column(UUID(as_uuid=True), ForeignKey("students.id"), primary_key=True)
    is_present = Column(Boolean, default=True)
    absence_reason = Column(Enum(AbsenceReasonEnum), nullable=True)

    attendance = relationship("Attendance")
    student = relationship("Student")


class Attendance(Base):
    __tablename__ = "attendances"
    id = Column(UUID(as_uuid=True), primary_key=True)
    date = Column(Date, nullable=False)
    is_rainy_day = Column(Boolean, nullable=False, default=False)
    attendance_details = relationship("AttendanceDetail", back_populates="attendance")
