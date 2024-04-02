from app.services.school import PreceptorService
from app.services.school import SchoolService
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
        self.school_service = SchoolService()
        self.teacher_service = TeacherService()
        self.preceptor_service = PreceptorService()

    def test_create_school(self):

        response = self.client.post(
            "/api/v1/school", json=self.school, headers=self.headers
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
