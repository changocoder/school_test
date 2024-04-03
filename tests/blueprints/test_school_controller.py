from app.services.school import ClassroomService
from app.services.school import CourseService
from app.services.school import PreceptorService
from app.services.school import SchoolService
from app.services.school import StudentService
from app.services.school import TeacherService
from tests.base_test import ShcoolDBTest


class TestSchoolController(ShcoolDBTest):
    def setUp(self):
        super().setUp()
        self.school = {
            "name": "Test School",
            "address": "Test Address",
            "phone": "123456789",
        }
        self.teacher_data = {
            "name": "Test Teacher",
            "last_name": "Test Last Name",
            "document": "123456789",
            "specialty": "Test Specialty",
        }
        self.preceptor_data = {
            "name": "Test Preceptor",
            "last_name": "Test Last Name",
            "document": "123456789",
        }
        self.student_data = {
            "name": "Test Student",
            "last_name": "Test Last Name",
            "document": "123456789",
            "email": "sarasa@test.com",
            "nationality": "Argentino",
        }

        self.school_service = SchoolService()
        self.teacher_service = TeacherService()
        self.preceptor_service = PreceptorService()
        self.student_service = StudentService()
        self.classroom_service = ClassroomService()
        self.course_service = CourseService()

    def test_create_school(self):

        response = self.client.post(
            "/api/v1/school/", json=self.school, headers=self.headers
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json["name"], self.school["name"])
        self.assertEqual(response.json["address"], self.school["address"])
        self.assertEqual(response.json["phone"], self.school["phone"])

    def test_get_school(self):
        school_obj = self.school_service.create(**self.school)

        response = self.client.get(
            f"/api/v1/school/{school_obj.id}", headers=self.headers
        )

        self.assertEqual(response.status_code, 200)

    def test_create_teacher_controller(self):
        school_obj = self.school_service.create(**self.school)
        teacher = {
            "name": "Test Teacher",
            "last_name": "Test Last Name",
            "document": "123456789",
            "specialty": "Test Specialty",
            "school_id": str(school_obj.id),
        }

        response = self.client.post(
            "/api/v1/teacher/", json=teacher, headers=self.headers
        )

        self.assertEqual(response.status_code, 201)

    def test_get_teacher_controller(self):
        school_obj = self.school_service.create(**self.school)
        teacher = {
            "name": "Test Teacher",
            "last_name": "Test Last Name",
            "document": "123456789",
            "specialty": "Test Specialty",
            "school_id": str(school_obj.id),
        }
        teacher_obj = self.teacher_service.create(**teacher)

        response = self.client.get(
            f"/api/v1/teacher/{teacher_obj.id}", headers=self.headers
        )

        self.assertEqual(response.status_code, 200)

    def test_create_student_with_school(self):
        school = self.school_service.create(
            name="Test School", address="Test Address", phone="123456789"
        )

        student = {
            "name": "Test Student",
            "last_name": "Test Last Name",
            "document": "123456789",
            "email": "student@test.com",
            "nationality": "Test Nationality",
            "school_id": str(school.id),
        }

        response = self.client.post(
            "/api/v1/student/", json=student, headers=self.headers
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json["name"], student["name"])

    def test_get_student_with_school(self):
        school = self.school_service.create(
            name="Test School", address="Test Address", phone="123456789"
        )
        student = {
            "name": "Test Student",
            "last_name": "Test Last Name",
            "document": "123456789",
            "email": "student@test.com",
            "nationality": "Test Nationality",
            "school_id": str(school.id),
        }
        student_obj = self.student_service.create(**student)

        response = self.client.get(
            f"/api/v1/student/{student_obj.id}", headers=self.headers
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["name"], student["name"])

    def test_create_course(self):
        school_obj = self.school_service.create(**self.school)
        teacher_obj = self.teacher_service.create(**self.teacher_data)
        preceptor_obj = self.preceptor_service.create(**self.preceptor_data)

        course = {
            "name": "Test Course",
            "school_id": str(school_obj.id),
            "teacher_id": str(teacher_obj.id),
            "preceptor_id": str(preceptor_obj.id),
        }

        response = self.client.post(
            "/api/v1/course/", json=course, headers=self.headers
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json["name"], course["name"])

    def test_get_course(self):
        school_obj = self.school_service.create(**self.school)
        teacher_obj = self.teacher_service.create(**self.teacher_data)
        preceptor_obj = self.preceptor_service.create(**self.preceptor_data)
        course = {
            "name": "Test Course",
            "school_id": str(school_obj.id),
            "teacher_id": str(teacher_obj.id),
            "preceptor_id": str(preceptor_obj.id),
        }
        course_obj = self.course_service.create(**course)

        response = self.client.get(
            f"/api/v1/course/{course_obj.id}", headers=self.headers
        )

        self.assertEqual(response.status_code, 200)

    def test_create_classroom(self):
        classroom = {
            "name": "Test Classroom",
        }

        response = self.client.post(
            "/api/v1/classroom/", json=classroom, headers=self.headers
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json["name"], classroom["name"])

    def test_get_classroom(self):
        classroom = {
            "name": "Test Classroom",
        }
        classroom_obj = self.classroom_service.create(**classroom)

        response = self.client.get(
            f"/api/v1/classroom/{classroom_obj.id}", headers=self.headers
        )

        self.assertEqual(response.status_code, 200)

    def test_create_preceptor_controller(self):
        response = self.client.post(
            "/api/v1/preceptor/", json=self.preceptor_data, headers=self.headers
        )

        self.assertEqual(response.status_code, 201)

    def test_get_preceptor_controller(self):
        preceptor_obj = self.preceptor_service.create(**self.preceptor_data)

        response = self.client.get(
            f"/api/v1/preceptor/{preceptor_obj.id}", headers=self.headers
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["name"], self.preceptor_data["name"])

    def test_enroll_student_controller(self):
        school_obj = self.school_service.create(**self.school)
        teacher_obj = self.teacher_service.create(**self.teacher_data)
        preceptor_obj = self.preceptor_service.create(**self.preceptor_data)
        self.student_data["school_id"] = str(school_obj.id)
        student_obj = self.student_service.create(**self.student_data)

        course = {
            "name": "Test Course",
            "school_id": str(school_obj.id),
            "teacher_id": str(teacher_obj.id),
            "preceptor_id": str(preceptor_obj.id),
        }

        course_obj = self.course_service.create(**course)

        data = {
            "course_id": str(course_obj.id),
            "student_id": str(student_obj.id),
        }

        response = self.client.post(
            "/api/v1/course/enroll-student", json=data, headers=self.headers
        )

        self.assertEqual(response.status_code, 204)
