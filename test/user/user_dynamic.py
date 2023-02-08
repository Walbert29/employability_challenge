from fastapi.testclient import TestClient
from src.main import app

user = TestClient(app)


def test_get_by_email():
    email_test = "challenge@demool.com"
    response = user.get(f"user/email/{email_test}")
    assert response.status_code == 200


test_get_by_email()
