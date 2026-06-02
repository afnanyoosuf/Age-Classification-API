from app import app
import pytest


@pytest.fixture
def client():
    app.testing = True

    with app.test_client() as client:
        yield client


# Test 1: Valid Adult
def test_valid_adult(client):

    response = client.post(
        '/predict',
        json={"age": 22}
    )

    assert response.status_code == 200
    assert response.json["You Are"] == "adult"


# Test 2: Valid Child
def test_valid_child(client):

    response = client.post(
        '/predict',
        json={"age": 10}
    )

    assert response.status_code == 200
    assert response.json["You Are"] == "child"


# Test 3: Valid Senior
def test_valid_senior(client):

    response = client.post(
        '/predict',
        json={"age": 75}
    )

    assert response.status_code == 200
    assert response.json["You Are"] == "senior"


# Test 4: Missing Age
def test_missing_age(client):

    response = client.post(
        '/predict',
        json={}
    )

    assert response.status_code == 400
    assert response.json["error"] == "age is required"


# Test 5: Invalid Type
def test_invalid_type(client):

    response = client.post(
        '/predict',
        json={"age": "abc"}
    )

    assert response.status_code == 400
    assert response.json["error"] == "age must be integer"


# Test 6: Invalid Range
def test_invalid_range(client):

    response = client.post(
        '/predict',
        json={"age": -5}
    )

    assert response.status_code == 400
    assert response.json["error"] == "age must be between 0 and 100"