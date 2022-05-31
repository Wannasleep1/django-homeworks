import pytest
from model_bakery import baker

from rest_framework.test import APIClient

from students.models import Student, Course


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def student_factory():

    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)

    return factory


@pytest.fixture
def course_factory():

    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)

    return factory


# Тест получения первого курса
@pytest.mark.django_db
def test_get_course(client, course_factory):
    course = course_factory(_quantity=1)
    response = client.get(f'/api/v1/courses/{course[0].id}/')
    data = response.json()

    assert response.status_code == 200
    assert course[0].name == data["name"]


# Тест получения списка курсов
@pytest.mark.django_db
def test_get_courses(client, course_factory):
    courses = course_factory(_quantity=10)
    response = client.get('/api/v1/courses/')
    data = response.json()

    assert response.status_code == 200
    for i, el in enumerate(data):
        assert el["name"] == courses[i].name


# Тест фильтрации курсов по id
@pytest.mark.django_db
def test_filter_by_id(client, course_factory):
    courses = course_factory(_quantity=10)
    response = client.get(f'/api/v1/courses/', data={'id': courses[3].id})
    data = response.json()

    assert response.status_code == 200
    assert len(data) == 1
    assert data[0]['id'] == courses[3].id


# Тест фильтрации курсов по name
@pytest.mark.django_db
def test_filter_by_name(client, course_factory):
    courses = baker.make_recipe("students.course_rec", _quantity=10)
    response = client.get(f'/api/v1/courses/', data={'name': 'Course_5'})
    data = response.json()

    assert response.status_code == 200
    assert len(data) == 1
    assert data[0]['name'] == 'Course_5'


# Тест успешного создания курса
@pytest.mark.django_db
def test_create_course(client):
    response = client.post("/api/v1/courses/", data={"name": "Test_name"})
    assert response.status_code == 201


# Тест успешного обновления курса
@pytest.mark.django_db
def test_update_course(client, course_factory):
    course = course_factory(_quantity=1)
    response = client.patch(f"/api/v1/courses/{course[0].id}/", data={'name': 'Another_name'})
    assert response.status_code == 200


# Тест успешного удаления курса
@pytest.mark.django_db
def test_delete_course(client, course_factory):
    course = course_factory(_quantity=1)
    response = client.delete(f"/api/v1/courses/{course[0].id}/")
    assert response.status_code == 204


# Тест валидации
@pytest.mark.django_db
@pytest.mark.parametrize("test_input,expected", [(20, 201), (1, 400)])
def test_students_validation(test_input, expected, client, student_factory, settings):
    settings.MAX_STUDENTS_PER_COURSE = test_input
    students = [el.id for el in student_factory(_quantity=2)]
    response = client.post("/api/v1/courses/", data={"name": "Course_name", "students": students})
    assert response.status_code == expected
