import logging

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from src.models.vacancy import VacancyModel
from src.schemas.vacancy import VacancySchema

# GET


def get_vacancy_by_id(db: Session, vacancy_id: str):

    try:
        """
        This function is responsible for extracting the data of a vacancy based on its id

        Args:
            db (Session): Session DB
            vacancy_id (str): Vacancy ID

        Returns:
            VacancyModel
        """
        vacancy = (
            db.query(VacancyModel).filter(VacancyModel.vacancy_id == vacancy_id).first()
        )

        return vacancy

    except Exception as error:
        logging.error(f"error getting the vacancy by id, error: {error}")
        raise error


def get_all_vacancies(db: Session):

    try:
        """
        This function is responsible for extracting all vacancies in the database

        Args:
            db (Session): Session DB

        Returns:
            List[VacancyModel]
        """
        vacancies = db.query(VacancyModel).all()

        return vacancies

    except Exception as error:
        logging.error(f"error getting all vacancies, error: {error}")
        raise error


# POST


def create_vacancy(db: Session, vacancy_data_in: VacancySchema):

    try:
        """
        This function is responsible for creating vacancy in the database

        Args:
            db (Session): Session DB
            vacancy_data_in (VacancySchema): Vacancy Data

        Returns:
            VacancyModel
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
        This function is responsible for deleting vacancy in the database

        Args:
            db (Session): Session DB
            vacancy_id (str): Vacancy ID

        Returns:
            VacancyModel
        """
        vacancy = (
            db.query(VacancyModel).filter(VacancyModel.vacancy_id == vacancy_id).first()
        )

        db.query(VacancyModel).filter(VacancyModel.vacancy_id == vacancy_id).delete()

        db.commit()

        return vacancy

    except Exception as error:
        logging.error(f"error deleting the vacancy, error: {error.args}")
        raise error
