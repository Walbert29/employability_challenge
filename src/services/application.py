import logging

from fastapi import HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from core.database import create_session
from crud import application, user, vacancy
from schemas.application import ApplicationSchema

vacancy_no_found = "Vacancy not found"
user_no_found = "User not found"


def get_applications_by_user_id(user_id: str):
    """
    This function is in charge of searching for the applications that a user has and creating a resulting json with the list of them

    Args:
        user_id (str): User ID

    Returns:
        JSON List Postulations
    """
    try:
        db = create_session()

        # Search and verify the existence of the user

        user_data = user.get_user_by_id(db=db, user_id=user_id)

        if user_data is None:
            return JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND,
                content={"message": user_no_found},
            )

        # Search and verify the applications you have stored

        applications_user = jsonable_encoder(
            application.get_applications_by_user_id(db=db, user_id=user_id)
        )

        if applications_user == []:
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content={"message": "The user has no applications"},
            )

        # Build the JSON with the list of the user's applications

        data_applications = []

        for application_data in applications_user:
            current_application = {
                "postulation_id": application_data.get("ApplicationModel").get("id"),
                "vacancy": application_data.get("VacancyModel"),
            }
            data_applications.append(current_application)

        return jsonable_encoder(data_applications)

    except Exception as error:
        logging.error(f"services: get_applications_by_user_id => {error}")
        raise HTTPException(
            status_code=status.HTTP_424_FAILED_DEPENDENCY,
            detail={"message": error.args},
        )
    finally:
        db.close()


def get_applications_by_vacancy_id(vacancy_id: str):
    """
    This function is in charge of searching for the users that a vacancy has and creating a resulting json with the list of them

    Args:
        vacancy_id (str): Vacancy ID

    Returns:
        JSON List Postulations
    """
    try:
        db = create_session()

        # Search and verify the existence of the vacancy

        vacancy_data = vacancy.get_vacancy_by_id(db=db, vacancy_id=vacancy_id)

        if vacancy_data is None:
            return JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND,
                content={"message": vacancy_no_found},
            )

        # Search and verify the applications you have stored

        applications_vacancy = jsonable_encoder(
            application.get_applications_by_vacancy_id(db=db, vacancy_id=vacancy_id)
        )

        if applications_vacancy == []:
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content={"message": "The vacancy has no applications"},
            )

        # Build the JSON with the list of users applying for the vacancy

        data_applications = []

        for application_data in applications_vacancy:
            current_application = {
                "postulation_id": application_data.get("ApplicationModel").get("id"),
                "user": application_data.get("UserModel"),
            }
            data_applications.append(current_application)

        return jsonable_encoder(data_applications)

    except Exception as error:
        logging.error(f"services: get_applications_by_vacancy_id => {error}")
        raise HTTPException(
            status_code=status.HTTP_424_FAILED_DEPENDENCY,
            detail={"message": error.args},
        )
    finally:
        db.close()


def create_application(data_application_in: ApplicationSchema):
    """
    This function is responsible for creating the applications

    Args:
        data_application_in (ApplicationSchema): Application Data

    Returns:
        ApplicationSchema
    """
    try:
        db = create_session()

        return application.create_application(
            db=db, data_application_in=data_application_in
        )

    except Exception as error:
        db.rollback()
        logging.error(f"services: create_application => {error}")
        raise HTTPException(
            status_code=status.HTTP_424_FAILED_DEPENDENCY,
            detail={"message": error.args},
        )
    finally:
        db.close()
