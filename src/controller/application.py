from fastapi import APIRouter, status

from services.application import (
    get_applications_by_user_id,
    get_applications_by_vacancy_id,
)

application_router = APIRouter(prefix="/application")

# GET


@application_router.get(
    "/user/{user_id}",
    tags=["Application"],
    status_code=status.HTTP_200_OK,
    summary="Returns the applications that the user has",
)
def get_application_by_user_id(user_id: str):
    """
    This controller is responsible for returning the applications that have a user in bas based on their id

    Method:
        GET

    Args:
        user_id (int): User ID

    Returns:
        List[ApplicationSchema]
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
    This controller is responsible for returning the applications that have a vacancy in bas based on their id

    Method:
        GET

    Args:
        vacancy_id (str): Vacancy ID

    Returns:
        List[ApplicationSchema]
    """
    return get_applications_by_vacancy_id(vacancy_id=vacancy_id)
