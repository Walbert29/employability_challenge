from services import vacancy
from schemas.vacancy import VacancySchema
from fastapi import APIRouter, status


vacancy_router = APIRouter(prefix="/vacancy")

# GET

@vacancy_router.get(
    "/{vacancy_id}",
    tags=["Vacancy"],
    status_code=status.HTTP_200_OK,
    summary="Return a vacancy by id",
)
def get_vacancy_by_id(vacancy_id: str):
    """
    GET vacancy by Vacancy ID

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
    CREATE a vacancy in database

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
def delete_vacancy_by_vacancy_id(vacancy_id:str):
    """
    DELETE a vacancy from database

    Returns:
        VacancySchema
    """
    return vacancy.delete_vacancy_by_id(vacancy_id=vacancy_id)
