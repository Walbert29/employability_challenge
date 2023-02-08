import logging
from crud import vacancy
from core.database import create_session
from fastapi import status, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from schemas.vacancy import VacancySchema

vacancy_no_found = "Vacancy not found"

def get_vacancy_by_vacancy_id(vacancy_id: str):
    """
    This method is responsible for extracting all the information of a user based on his id
    """
    try:
        db = create_session()

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
    This method is responsible for creating a user with their respective information in the database
    """
    try:
        db = create_session()

        return vacancy.create_vacancy(db= db, vacancy_data_in=data_vacancy_in)

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
    This method is responsible of delete a user
    """
    try:
        db = create_session()

        """
        Check if a vacancy exists
        """

        vacancy_data = vacancy.get_vacancy_by_id(db=db, vacancy_id=vacancy_id)

        if vacancy_data is None:
            return JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND,
                content={"message": vacancy_no_found},
            )

        return vacancy.delete_vacancy_by_id(db= db, vacancy_id=vacancy_id)

    except Exception as error:
        db.rollback()
        logging.error(f"services: delete_vacancy_by_id => {error}")
        raise HTTPException(
            status_code=status.HTTP_424_FAILED_DEPENDENCY,
            detail={"message": error.args},
        )
    finally:
        db.close()