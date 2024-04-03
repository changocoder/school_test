from app.services.school import AttendanceService
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

    def test_disable_student_controller(self):
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

        response = self.client.put(
            f"/api/v1/student/{student_obj.id}/disable", headers=self.headers, json=data
        )

        self.assertEqual(response.status_code, 204)


class TestAttendanceController(ShcoolDBTest):
    def setUp(self):
        super().setUp()
        self.school_service = SchoolService()
        self.teacher_service = TeacherService()
        self.preceptor_service = PreceptorService()
        self.student_service = StudentService()
        self.classroom_service = ClassroomService()
        self.course_service = CourseService()
        self.attendance_service = AttendanceService()

        self.school_data = {
            "name": "Test School",
            "address": "Test Address",
            "phone": "123456789",
        }
        self.school_data2 = {
            "name": "Test School2",
            "address": "Test Address",
            "phone": "123456789",
        }
        self.school_obj = self.school_service.create(**self.school_data)
        self.school_obj2 = self.school_service.create(**self.school_data2)
        self.teacher_data = {
            "name": "Test Teacher",
            "last_name": "Test Last Name",
            "document": "123456783",
            "specialty": "Test Specialty",
            "school_id": str(self.school_obj.id),
        }
        self.teacher_obj = self.teacher_service.create(**self.teacher_data)
        self.preceptor_data = {
            "name": "Test Preceptor",
            "last_name": "Test Last Name",
            "document": "123456784",
            "school_id": str(self.school_obj.id),
        }
        self.preceptor_obj = self.preceptor_service.create(**self.preceptor_data)
        self.course_data = {
            "name": "Test Course",
            "school_id": str(self.school_obj.id),
            "teacher_id": str(self.teacher_obj.id),
            "preceptor_id": str(self.preceptor_obj.id),
        }
        self.course_data2 = {
            "name": "Test Course2",
            "school_id": str(self.school_obj.id),
            "teacher_id": str(self.teacher_obj.id),
            "preceptor_id": str(self.preceptor_obj.id),
        }

        self.course_obj = self.course_service.create(**self.course_data)
        self.course_obj2 = self.course_service.create(**self.course_data2)
        self.student_data = {
            "name": "Test Student",
            "last_name": "Test Last Name",
            "document": "123456789",
            "email": "test@test.com",
            "nationality": "Argentino",
            "school_id": str(self.school_obj.id),
            "course_id": str(self.course_obj.id),
        }

        self.student_data_2 = {
            "name": "Student2",
            "last_name": "Last Name2",
            "document": "123456781",
            "email": "test1@test.com",
            "nationality": "Argentino",
            "school_id": str(self.school_obj.id),
            "course_id": str(self.course_obj.id),
        }

        self.student_data_2 = {
            "name": "Student2",
            "last_name": "Last Name2",
            "document": "123456781",
            "email": "test1@test.com",
            "nationality": "Argentino",
            "school_id": str(self.school_obj.id),
            "course_id": str(self.course_obj.id),
        }
        self.student_data_3 = {
            "name": "Student2",
            "last_name": "Last Name2",
            "document": "123456786",
            "email": "test3@test.com",
            "nationality": "Argentino",
            "is_active": False,
            "school_id": str(self.school_obj.id),
            "course_id": str(self.course_obj.id),
        }

        self.student_obj = self.student_service.create(**self.student_data)
        self.student_obj_2 = self.student_service.create(**self.student_data_2)
        self.student_obj_3 = self.student_service.create(**self.student_data_3)

    def test_create_attendance_controller(self):
        data = {
            "course_id": str(self.course_obj.id),
            "date": "2024-03-01",
            "students": [
                {
                    "student_id": str(self.student_obj.id),
                    "is_present": True,
                },
                {
                    "student_id": str(self.student_obj_2.id),
                    "is_present": False,
                    "reason_absence": "ILLNESS",
                },
            ],
        }
        response = self.client.post(
            "/api/v1/attendance/", json=data, headers=self.headers
        )

        self.assertEqual(response.status_code, 201)

    def test_get_attendance_controller(self):
        data = {
            "course_id": str(self.course_obj.id),
            "date": "2024-03-01",
            "students": [
                {
                    "student_id": str(self.student_obj.id),
                    "is_present": True,
                },
                {
                    "student_id": str(self.student_obj_2.id),
                    "is_present": False,
                    "reason_absence": "ILLNESS",
                },
            ],
        }
        attendance_obj = self.attendance_service.create_attendance_and_detail(data)

        response = self.client.get(
            f"/api/v1/attendance/{attendance_obj.id}", headers=self.headers
        )

        self.assertEqual(response.status_code, 200)

    def test_update_attendance_controller(self):
        data = {
            "course_id": str(self.course_obj2.id),
            "date": "2024-03-01",
            "students": [
                {
                    "student_id": str(self.student_obj.id),
                    "is_present": True,
                },
                {
                    "student_id": str(self.student_obj_2.id),
                    "is_present": False,
                    "reason_absence": "ILLNESS",
                },
            ],
        }
        update_data = data.copy()

        attendance_obj = self.attendance_service.create_attendance_and_detail(data)

        update_data["students"][0]["is_present"] = False
        update_data["students"][0]["reason_absence"] = "OTHER"
        update_data["course_id"] = str(self.course_obj2.id)

        response = self.client.put(
            f"/api/v1/attendance/{attendance_obj.id}",
            json=update_data,
            headers=self.headers,
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["course"]["id"], str(self.course_obj2.id))

        # search in json response the student with id of student_obj.id
        student = next(
            student
            for student in response.json["attendance_details"]
            if student["student"]["id"] == str(self.student_obj.id)
        )
        student_2 = next(
            student
            for student in response.json["attendance_details"]
            if student["student"]["id"] == str(self.student_obj_2.id)
        )
        self.assertEqual(student["absence_reason"], "OTHER")
        self.assertEqual(student_2["absence_reason"], "ILLNESS")

    def test_create_attendance_with_inactive_students(self):
        data = {
            "course_id": str(self.course_obj.id),
            "date": "2024-03-01",
            "students": [
                {
                    "student_id": str(self.student_obj.id),
                    "is_present": True,
                },
                {
                    "student_id": str(self.student_obj_2.id),
                    "is_present": False,
                    "reason_absence": "ILLNESS",
                },
                {
                    "student_id": str(self.student_obj_3.id),
                    "is_present": True,
                },
            ],
        }

        response = self.client.post(
            "/api/v1/attendance/", json=data, headers=self.headers
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(len(response.json["attendance_details"]), 2)

    def test_report_course_attendance(self):
        data = {
            "course_id": str(self.course_obj.id),
            "date": "2024-03-01",
            "students": [
                {
                    "student_id": str(self.student_obj.id),
                    "is_present": True,
                },
                {
                    "student_id": str(self.student_obj_2.id),
                    "is_present": False,
                    "reason_absence": "ILLNESS",
                },
                {
                    "student_id": str(self.student_obj_3.id),
                    "is_present": True,
                },
            ],
        }
        data2 = {
            "course_id": str(self.course_obj.id),
            "date": "2024-03-02",
            "students": [
                {
                    "student_id": str(self.student_obj.id),
                    "is_present": True,
                },
                {
                    "student_id": str(self.student_obj_2.id),
                    "is_present": False,
                    "reason_absence": "ILLNESS",
                },
                {
                    "student_id": str(self.student_obj_3.id),
                    "is_present": True,
                },
            ],
        }
        self.attendance_service.create_attendance_and_detail(data)
        self.attendance_service.create_attendance_and_detail(data2)

        response = self.client.get(
            f"/api/v1/course/{self.course_obj.id}/report-attendance/?date_attendance=2024-03-01",
            headers=self.headers,
        )

        self.assertEqual(response.status_code, 200)

    def test_report_course_attendance_without_date_param(self):
        data = {
            "course_id": str(self.course_obj.id),
            "date": "2024-03-01",
            "students": [
                {
                    "student_id": str(self.student_obj.id),
                    "is_present": True,
                },
                {
                    "student_id": str(self.student_obj_2.id),
                    "is_present": False,
                    "reason_absence": "ILLNESS",
                },
                {
                    "student_id": str(self.student_obj_3.id),
                    "is_present": True,
                },
            ],
        }
        data2 = {
            "course_id": str(self.course_obj.id),
            "date": "2024-03-02",
            "students": [
                {
                    "student_id": str(self.student_obj.id),
                    "is_present": True,
                },
                {
                    "student_id": str(self.student_obj_2.id),
                    "is_present": False,
                    "reason_absence": "ILLNESS",
                },
                {
                    "student_id": str(self.student_obj_3.id),
                    "is_present": True,
                },
            ],
        }
        self.attendance_service.create_attendance_and_detail(data)
        self.attendance_service.create_attendance_and_detail(data2)

        response = self.client.get(
            f"/api/v1/course/{self.course_obj.id}/report-attendance/?date_attendance=2024-03-02",
            headers=self.headers,
        )

        self.assertEqual(response.status_code, 200)
