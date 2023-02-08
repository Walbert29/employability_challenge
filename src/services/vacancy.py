import logging

from fastapi import HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from src.core.database import create_session
from src.crud import vacancy
from src.schemas.vacancy import VacancySchema

vacancy_no_found = "Vacancy not found"


def get_vacancy_by_vacancy_id(vacancy_id: str):
    """
    This function is in charge of searching and displaying the information of a vacancy

    Args:
        vacancy_id (str): Vacancy ID

    Returns:
        VacancySchema
    """
    try:
        db = create_session()

        # Check if a user exists

        vacancy_data = vacancy.get_vacancy_by_id(db=db, vacancy_id=vacancy_id)

        if vacancy_data is None:
            return JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND,
                content={"message": vacancy_no_found},
            )

        return jsonable_encoder(vacancy_data)

    except Exception as error:
        logging.error(f"services: get_vacancy_by_user_id => {error}")
        raise HTTPException(
            status_code=status.HTTP_424_FAILED_DEPENDENCY,
            detail={"message": error.args},
        )
    finally:
        db.close()


def create_vacancy(data_vacancy_in: VacancySchema):
    """
    This function is responsible for creating the vacancy in the database

    Args:
        data_vacancy_in (VacancySchema): Vacancy Data

    Returns:
        VacancySchema
    """
    try:
        db = create_session()

        return vacancy.create_vacancy(db=db, vacancy_data_in=data_vacancy_in)

    except Exception as error:
        db.rollback()
        logging.error(f"services: create_vacancy => {error}")
        raise HTTPException(
            status_code=status.HTTP_424_FAILED_DEPENDENCY,
            detail={"message": error.args},
        )
    finally:
        db.close()


def delete_vacancy_by_id(vacancy_id: str):
    """
    This function is responsible for removing the vacancy from the database

    Args:
        vacancy_id (str): Vacancy ID

    Returns:
        VacancySchema
    """
    try:
        db = create_session()

        # Check if a vacancy exists

        vacancy_data = vacancy.get_vacancy_by_id(db=db, vacancy_id=vacancy_id)

        if vacancy_data is None:
            return JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND,
                content={"message": vacancy_no_found},
            )

        return vacancy.delete_vacancy_by_id(db=db, vacancy_id=vacancy_id)

    except Exception as error:
        db.rollback()
        logging.error(f"services: delete_vacancy_by_id => {error}")
        raise HTTPException(
            status_code=status.HTTP_424_FAILED_DEPENDENCY,
            detail={"message": error.args},
        )
    finally:
        db.close()
