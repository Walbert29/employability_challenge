import json
from fastapi.testclient import TestClient
from src.main import app

user = TestClient(app)


def test_vacancy_by_id():
    id_test = "38d87e5c-73c5-4ee4-a071-1d324bbb91b9"
    response = user.get(f"vacancy/{id_test}")
    assert response.status_code == 200
    assert response.json() == {
      "company_name": "Facebook",
      "vacancy_id": "38d87e5c-73c5-4ee4-a071-1d324bbb91b9",
      "currency": "COP",
      "load_date": "2023-02-08",
      "vacancy_link": "www.facebook.com",
      "position_name": "Dev",
      "salary": 1000000,
      "required_skills": [
        {
          "name": "Python",
          "experience": 10
        }
      ]
    }


def test_create_vacancy():
    data_to_create = {
      "vacancy_link": "www.google.com/jobs",
      "position_name": "Developer",
      "company_name": "Google",
      "salary": 1000,
      "currency": "USD",
      "required_skills": [
        {
          "name": "Python",
          "experience": 10
        }
      ],
      "load_date": "2023-02-08T03:45:11.354573"
    }
    response = user.post("vacancy/create", data=json.dumps(data_to_create))
    assert response.status_code == 201
    assert response.json() == {
      "company_name": "Google",
      "vacancy_id": response.json().get("vacancy_id"),
      "currency": "USD",
      "load_date": "2023-02-08",
      "vacancy_link": "www.google.com/jobs",
      "position_name": "Developer",
      "salary": 1000,
      "required_skills": [
        {
          "name": "Python",
          "experience": 10
        }
      ]
    }


def test_delete_vacancy():
    vacancy_id = "4e1b0d49-da7d-4642-a728-850476bfb38d"
    response = user.put(f"vacancy/delete/{vacancy_id}")
    assert response.status_code == 200
    assert response.json() == {
      "company_name": "Google",
      "vacancy_id": "4e1b0d49-da7d-4642-a728-850476bfb38d",
      "currency": "USD",
      "load_date": "2023-02-08",
      "vacancy_link": "www.google.com/jobs",
      "position_name": "Developer",
      "salary": 1000,
      "required_skills": [
        {
          "name": "Python",
          "experience": 10
        }
      ]
    }