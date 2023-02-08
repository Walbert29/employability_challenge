from services.application import get_applications_by_user_id, get_applications_by_vacancy_id
from fastapi import APIRouter, status


application_router = APIRouter(prefix="/application")

# GET

@application_router.get(
    "/user/{user_id}",
    tags=["Application"],
    status_code=status.HTTP_200_OK,
    summary="Return application from user",
)
def get_application_by_user_id(user_id: str):
    """
    GET user by User email

    Returns:
        UserSchema
    """
    return get_applications_by_user_id(user_id=user_id)


@application_router.get(
    "/vacancy/{vacancy_id}",
    tags=["Application"],
    status_code=status.HTTP_200_OK,
    summary="Return application from vacancy",
)
def get_application_by_vacancy_id(vacancy_id: str):
    """
    GET user by User email

    Returns:
        UserSchema
    """
    return get_applications_by_vacancy_id(vacancy_id=vacancy_id)

