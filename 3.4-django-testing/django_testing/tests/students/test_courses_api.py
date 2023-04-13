
import pytest
from rest_framework.test import APIClient
from model_bakery import baker
from students.models import Student, Course

def test_example():
    assert True

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

@pytest.mark.django_db
def test_get_first_course(client, course_factory):
    cour = course_factory(_quantity=5)
    response = client.get('/api/v1/courses/')
    assert response.status_code == 200
    data = response.json()
    assert data[0]['name'] == cour[0].name

@pytest.mark.django_db
def test_get_list_course(client, course_factory):
    cour = course_factory(_quantity=5)
    response = client.get('/api/v1/courses/')
    assert response.status_code == 200
    data = response.json()
    assert len(data) == len(cour)

@pytest.mark.django_db
def test_filter_id_course(client, course_factory):
    cour = course_factory(_quantity=5)
    id = Course.objects.all().first().id
    response = client.get(f'/api/v1/courses/{id}/')
    assert response.status_code == 200
    data = response.json()
    data2 = Course.objects.filter(id=11)
    assert data2[0].id == data['id']
    assert data2[0].name == data['name']

@pytest.mark.django_db
def test_filter_name_course(client, course_factory):
    cour = Course.objects.create(id=16, name='Course_1')
    response = client.get('/api/v1/courses/', {'name': cour.name})
    assert response.status_code == 200
    data = response.json()
    assert data[0]['name'] == cour.name
    assert data[0]['id'] == cour.id

@pytest.mark.django_db
def test_create_course(client):
    cour = Course.objects.create(id=17, name='Course_2')
    response = client.get('/api/v1/courses/')
    assert response.status_code == 200
    data = response.json()
    assert data[0]['name'] == cour.name
    assert data[0]['id'] == cour.id

@pytest.mark.django_db
def test_update_course(client, course_factory):
    cour = course_factory(_quantity=5)
    id = Course.objects.all().first().id
    response = client.patch(f'/api/v1/courses/{id}/', {'name': 'Course_all'})
    cour_fix = Course.objects.filter(id=id)
    assert response.status_code == 200
    data = response.json()
    assert cour_fix[0].name == data['name']

@pytest.mark.django_db
def test_delete_course(client, course_factory):
    cour = course_factory(_quantity=5)
    id = Course.objects.all().first().id
    response = client.delete(f'/api/v1/courses/{id}/')
    data = Course.objects.all()
    assert response.status_code == 204
    assert len(cour) != len(data)


