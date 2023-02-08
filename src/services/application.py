import logging
from crud import user, vacancy, application
from core.database import create_session
from fastapi import status, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from schemas.application import ApplicationSchema

vacancy_no_found = "Vacancy not found"
user_no_found = "User not found"

def get_applications_by_user_id(user_id: str):
    """
    This method is responsible for extracting all the information of a user based on his id
    """
    try:
        db = create_session()

        user_data = user.get_user_by_id(db=db, user_id=user_id)

        if user_data is None:
            return JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND,
                content={"message": user_no_found},
            )

        applications_user = jsonable_encoder(application.get_applications_by_user_id(db=db, user_id=user_id))

        if applications_user == []:
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content={"message": "The user has no applications"},
            )

        data_applications = []

        for application_data in applications_user:
            current_application = {
                "postulation_id":application_data.get("ApplicationModel").get("id"),
                "vacancy":application_data.get("VacancyModel")
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

        applications_vacancy = jsonable_encoder(application.get_applications_by_vacancy_id(db=db, vacancy_id=vacancy_id))

        if applications_vacancy == []:
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content={"message": "The vacancy has no applications"},
            )

        data_applications = []

        for application_data in applications_vacancy:
            current_application = {
                "postulation_id":application_data.get("ApplicationModel").get("id"),
                "user":application_data.get("UserModel")
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
    This method is responsible for creating a user with their respective information in the database
    """
    try:
        db = create_session()

        return application.create_application(db= db, data_application_in=data_application_in)

    except Exception as error:
        db.rollback()
        logging.error(f"services: create_application => {error}")
        raise HTTPException(
            status_code=status.HTTP_424_FAILED_DEPENDENCY,
            detail={"message": error.args},
        )
    finally:
        db.close()