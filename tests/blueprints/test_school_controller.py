from app.services.school import SchoolService
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
