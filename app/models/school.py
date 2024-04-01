from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import UUID
from sqlalchemy.orm import relationship

from app.models.db import Base


class Person(Base):
    __abstract__ = True
    name = Column(String)
    last_name = Column(String)
    document = Column(String, unique=True)


class Teacher(Person):
    __tablename__ = "teachers"
    specialty = Column(String)
    # Más atributos y relaciones si son necesarios


class Student(Person):
    __tablename__ = "students"
    email = Column(String, unique=True)
    nationality = Column(String)
    classroom_id = Column(UUID(as_uuid=True), ForeignKey("classroom.id"))
    classroom = relationship("Classroom", back_populates="students")


class Preceptor(Person):
    __tablename__ = "preceptors"
    # Atributos específicos del Preceptor


class Classroom(Base):
    __tablename__ = "classrooms"
    name = Column(String)
    students = relationship("Student", order_by=Student.id, back_populates="classroom")


class Course(Base):
    __tablename__ = "courses"
    name = Column(String)
    teacher_id = Column(UUID(as_uuid=True), ForeignKey("teacher.id"))
    teacher = relationship("Teacher")
    precetor_id = Column(UUID(as_uuid=True), ForeignKey("preceptor.id"))
    preceptor = relationship("Preceptor")
