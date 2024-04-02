from app.models.school import Course
from app.models.school import Preceptor
from app.models.school import School
from app.models.school import Student
from app.models.school import Teacher
from tests.base_test import ShcoolDBTest


class TestSchoolModels(ShcoolDBTest):
    def test_create_student(self):
        student = Student(
            name="John",
            last_name="Doe",
            document="12345679",
            email="sarasa@test.com",
            nationality="Argentino",
            is_active=True,
        )

        self.session.add(student)
        self.session.commit()

        student_inserted = self.session.query(Student).first()

        self.assertEqual(student_inserted.name, "John")
        self.assertEqual(student_inserted.last_name, "Doe")
        self.assertEqual(student_inserted.document, "12345679")
        self.assertEqual(student_inserted.email, "sarasa@test.com")
        self.assertEqual(student_inserted.nationality, "Argentino")
        self.assertTrue(student_inserted.is_active)

    def test_create_school(self):
        school = School(
            name="School",
            address="Av. Siempreviva 123",
            phone="123456789",
        )

        self.session.add(school)
        self.session.commit()

        school_inserted = self.session.query(School).first()

        self.assertEqual(school_inserted.name, "School")
        self.assertEqual(school_inserted.address, "Av. Siempreviva 123")
        self.assertEqual(school_inserted.phone, "123456789")

    def test_create_teacher_with_school(self):
        school = School(name="Test School", address="123 Main St", phone="123-456-7890")
        self.session.add(school)
        self.session.commit()

        teacher = Teacher(
            name="Alice",
            last_name="Smith",
            document="98765432",
            specialty="Mathematics",
            school_id=school.id,
        )

        self.session.add(teacher)
        self.session.commit()

        teacher_inserted = self.session.query(Teacher).first()

        self.assertEqual(teacher_inserted.name, "Alice")
        self.assertEqual(teacher_inserted.last_name, "Smith")
        self.assertEqual(teacher_inserted.document, "98765432")
        self.assertEqual(teacher_inserted.specialty, "Mathematics")
        self.assertEqual(teacher_inserted.school_id, school.id)

    def test_create_preceptor_with_school(self):
        school = School(name="Test School", address="123 Main St", phone="123-456-7890")
        self.session.add(school)
        self.session.commit()

        preceptor = Preceptor(
            name="Bob", last_name="Johnson", document="11223344", school_id=school.id
        )

        self.session.add(preceptor)
        self.session.commit()

        preceptor_inserted = self.session.query(Preceptor).first()

        self.assertEqual(preceptor_inserted.name, "Bob")
        self.assertEqual(preceptor_inserted.last_name, "Johnson")
        self.assertEqual(preceptor_inserted.document, "11223344")
        self.assertEqual(preceptor_inserted.school_id, school.id)

    def test_create_student_with_school(self):
        school = School(name="Test School", address="123 Main St", phone="123-456-7890")
        self.session.add(school)
        self.session.commit()

        student = Student(
            name="John",
            last_name="Doe",
            document="12345679",
            email="john@test.com",
            nationality="Argentino",
            is_active=True,
            school_id=school.id,
        )

        self.session.add(student)
        self.session.commit()

        student_inserted = self.session.query(Student).first()

        self.assertEqual(student_inserted.name, "John")
        # ... más asserts ...
        self.assertEqual(student_inserted.school_id, school.id)

    def test_create_course_with_school(self):
        school = School(name="Test School", address="123 Main St", phone="123-456-7890")
        self.session.add(school)
        self.session.commit()

        course = Course(name="History", school_id=school.id)

        self.session.add(course)
        self.session.commit()

        course_inserted = self.session.query(Course).first()

        self.assertEqual(course_inserted.name, "History")
        self.assertEqual(course_inserted.school_id, school.id)
