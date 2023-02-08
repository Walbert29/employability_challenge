import json
from fastapi.testclient import TestClient
from src.main import app

user = TestClient(app)


def test_get_by_email():
    email_test = "challenge@demool.com"
    response = user.get(f"user/email/{email_test}")
    assert response.status_code == 200
    assert response.json() == {
      "first_name": "Challenge",
      "email": "challenge@demool.com",
      "skills": [
        {
          "name": "Python",
          "experience": "10"
        }
      ],
      "update_date": "2023-02-07",
      "last_name": "Demo",
      "user_id": "a2d060f6-bda1-4326-9f3e-cc1c3da37805",
      "years_previous_experience": 5,
      "load_date": "2023-02-07"
    }


def test_get_by_user_id():
    id_test = "a2d060f6-bda1-4326-9f3e-cc1c3da37805"
    response = user.get(f"user/{id_test}")
    assert response.status_code == 200
    assert response.json() == {
      "first_name": "Challenge",
      "email": "challenge@demool.com",
      "skills": [
        {
          "name": "Python",
          "experience": "10"
        }
      ],
      "update_date": "2023-02-07",
      "last_name": "Demo",
      "user_id": "a2d060f6-bda1-4326-9f3e-cc1c3da37805",
      "years_previous_experience": 5,
      "load_date": "2023-02-07"
    }


def test_create_user():
    data_to_create = {
      "first_name": "Backend",
      "last_name": "Test",
      "email": "backend@test.com",
      "years_previous_experience": 1,
      "skills": [
        {
          "name": "Python",
          "experience": 10
        }
      ],
      "load_date": "2023-02-08T03:45:11.026579",
      "update_date": "2023-02-08T03:45:11.026579"
    }
    response = user.post(f"user/create", data=json.dumps(data_to_create))
    assert response.status_code == 201
    assert response.json() == {
      "first_name": "Backend",
      "email": "backend@test.com",
      "skills": [
        {
          "name": "Python",
          "experience": 10
        }
      ],
      "update_date": "2023-02-08",
      "last_name": "Test",
      "user_id": response.json().get("user_id"),
      "years_previous_experience": 1,
      "load_date": "2023-02-08"
    }


def test_update_user():
    user_id = "a2d060f6-bda1-4326-9f3e-cc1c3da37805"
    data_to_update = {
      "first_name": "Challenge",
      "last_name": "Demo",
      "years_previous_experience": 5,
      "skills": [
        {
          "name": "Python",
          "experience": 2
        }
      ],
      "update_date": "2023-02-08T03:45:11.026579"
    }
    response = user.put(f"user/update/{user_id}", data=json.dumps(data_to_update))
    assert response.status_code == 200
    assert response.json() == {
        "first_name": "Challenge",
        "email": "challenge@demool.com",
        "skills": [
            {
                "name": "Python",
                "experience": 2
            }
        ],
        "update_date": "2023-02-08",
        "last_name": "Demo",
        "user_id": response.json().get("user_id"),
        "years_previous_experience": 5,
        "load_date": "2023-02-08"
    }