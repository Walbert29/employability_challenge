import logging
from models.vacancy import VacancyModel
from schemas.vacancy import VacancySchema
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder


# GET

def get_vacancy_by_id(db: Session, vacancy_id: str):

    try:
        """
        GET a vacancy information based ID
        """
        vacancy = db.query(VacancyModel).filter(VacancyModel.vacancy_id == vacancy_id).first()

        return vacancy

    except Exception as error:
        logging.error(f"error getting the vacancy by id, error: {error}")
        raise error


# POST

def create_vacancy(db: Session, vacancy_data_in: VacancySchema):

    try:
        """
        POST for create a vacancy
        """

        json_data = jsonable_encoder(vacancy_data_in)

        data_to_create = VacancyModel(**json_data)

        db.add(data_to_create)

        db.commit()

        db.refresh(data_to_create)

        return data_to_create

    except Exception as error:
        logging.error(f"error creating the vacancy, error: {error.args}")
        raise error


# DELETE

def delete_vacancy_by_id(db: Session, vacancy_id: str):
    try:
        """
        DELETE vacancy from database
        """
        vacancy = db.query(VacancyModel).filter(VacancyModel.vacancy_id == vacancy_id).first()

        db.query(VacancyModel).filter(VacancyModel.vacancy_id == vacancy_id).delete()

        db.commit()

        return vacancy

    except Exception as error:
        logging.error(f"error deleting the vacancy, error: {error.args}")
        raise error
