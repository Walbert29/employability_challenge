from fastapi import APIRouter, status

from schemas.vacancy import VacancySchema
from services import vacancy

vacancy_router = APIRouter(prefix="/vacancy")

# GET


@vacancy_router.get(
    "/{vacancy_id}",
    tags=["Vacancy"],
    status_code=status.HTTP_200_OK,
    summary="Return the information of a vacancy based on its id",
)
def get_vacancy_by_id(vacancy_id: str):
    """
    This controller is responsible for returning all the information stored in the database of a vacancy

    Method:
        GET

    Args:
        vacancy_id (str): Vacancy ID

    Returns:
        VacancySchema
    """
    return vacancy.get_vacancy_by_vacancy_id(vacancy_id=vacancy_id)


# POST


@vacancy_router.post(
    "/create",
    tags=["Vacancy"],
    status_code=status.HTTP_201_CREATED,
    summary="Create a vacancy",
)
def create_vacancy(vacancy_data_in: VacancySchema):
    """
    This controller is in charge of creating a vacancy in the database

    Method:
        POST

    Args:
        vacancy_data_in (VacancySchema): Vacancy Data

    Returns:
        VacancySchema
    """
    return vacancy.create_vacancy(data_vacancy_in=vacancy_data_in)


# DELETE


@vacancy_router.delete(
    "/delete/{vacancy_id}",
    tags=["Vacancy"],
    status_code=status.HTTP_200_OK,
    summary="Delete a vacancy",
)
def delete_vacancy_by_vacancy_id(vacancy_id: str):
    """
    This controller is in charge of deleting a vacancy in the database

    Method:
        DELETE

    Args:
        vacancy_id (str): Vacancy ID

    Returns:
        VacancySchema
    """
    return vacancy.delete_vacancy_by_id(vacancy_id=vacancy_id)
