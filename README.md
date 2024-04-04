# School App
This is a school app that allows you to manage students, teachers, and courses. You can add, edit, and delete students, teachers, and courses. You can also assign students to courses and teachers to courses. You can also view the list of students, teachers, and courses.

## Installation
```bash
poetry install
```

## Run Tests
```bash
docker-compose -f docker-compose-test.yml run --rm --entrypoint="pytest -vv" school-api
```

## Run Server
```bash
docker-compose up --build -d
```
