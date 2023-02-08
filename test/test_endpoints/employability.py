from fastapi.testclient import TestClient
from src.main import app

user = TestClient(app)


def test_employability_by_user_id():

    # Define the data and url of the request

    user_id = "a91b867a-f2f7-4834-94aa-4052d76d6516"

    response = user.get(f"employability/user/{user_id}")

    # Take the test

    assert response.status_code == 200

    assert response.json() == [
      {
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
    ]