from fastapi.testclient import TestClient
from src.main import app

user = TestClient(app)


def test_application_by_user_id():

    # Define the data and url of the request

    user_id = "a2d060f6-bda1-4326-9f3e-cc1c3da37805"

    response = user.get(f"application/user/{user_id}")

    # Take the test

    assert response.status_code == 200

    assert response.json() == [
        {
            "postulation_id": 3,
            "vacancy": {
                "company_name": "Rappi",
                "vacancy_id": "216c862b-9458-44e9-82a7-8e5af900d99b",
                "currency": "COP",
                "load_date": "2023-02-07",
                "vacancy_link": "www.google.com",
                "position_name": "Dev",
                "salary": 1,
                "required_skills": [{"name": "Python", "experience": 5}],
            },
        }
    ]


def test_application_by_vacancy_id():

    # Define the data and url of the request

    vacancy_id = "216c862b-9458-44e9-82a7-8e5af900d99b"

    response = user.get(f"application/vacancy/{vacancy_id}")

    # Take the test

    assert response.status_code == 200

    assert response.json() == [
        {
            "postulation_id": 3,
            "user": {
                "first_name": "Challenge",
                "email": "challenge@demool.com",
                "skills": [{"name": "Python", "experience": 2}],
                "update_date": "2023-02-08",
                "last_name": "Demo",
                "user_id": "a2d060f6-bda1-4326-9f3e-cc1c3da37805",
                "years_previous_experience": 5,
                "load_date": "2023-02-08",
            },
        }
    ]
