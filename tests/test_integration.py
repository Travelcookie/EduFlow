import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json["app"] == "EduFlow"

def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "healthy"

def test_courses_list(client):
    response = client.get("/courses")
    assert response.status_code == 200
    assert response.json["count"] == 3

def test_course_detail_found(client):
    response = client.get("/courses/1")
    assert response.status_code == 200
    assert response.json["title"] == "DevOps Grundlagen"

def test_course_detail_not_found(client):
    response = client.get("/courses/999")
    assert response.status_code == 404