import logging
from models.application import ApplicationModel
from models.vacancy import VacancyModel
from models.user import UserModel
from schemas.application import ApplicationSchema
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder


# GET

def get_applications_by_user_id(db: Session, user_id: str):

    try:
        """
        GET applications by user ID
        """
        vacancies = db.query(ApplicationModel, VacancyModel).filter(ApplicationModel.user_id == user_id).filter(ApplicationModel.vacancy_id == VacancyModel.vacancy_id).all()

        return vacancies

    except Exception as error:
        logging.error(f"error getting the applications from user, error: {error}")
        raise error


def get_applications_by_vacancy_id(db: Session, vacancy_id: str):

    try:
        """
        GET vacancies by vacancy ID
        """
        vacancies = db.query(ApplicationModel, UserModel).filter(ApplicationModel.vacancy_id == vacancy_id).filter(ApplicationModel.user_id == UserModel.user_id).all()

        return vacancies

    except Exception as error:
        logging.error(f"error getting the applications from vacancy, error: {error}")
        raise error


# POST

def create_application(db: Session, application_data_in: ApplicationSchema):

    try:
        """
        POST create application
        """

        json_data = jsonable_encoder(application_data_in)

        data_to_create = ApplicationModel(**json_data)

        db.add(data_to_create)

        db.commit()

        db.refresh(data_to_create)

        return data_to_create

    except Exception as error:
        logging.error(f"error creating the application, error: {error.args}")
        raise error