import logging

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from src.models.user import UserModel
from src.schemas.user import UpdateUserSchema, UserSchema

# GET


def get_user_by_id(db: Session, user_id: str):

    try:
        """
        This function is responsible for fetching the user's information from the database on based user_id.

        Args:
            db (Session): Session DB
            user_id (str): User ID

        Returns:
            UserModel
        """
        user = db.query(UserModel).filter(UserModel.user_id == user_id).first()

        return user

    except Exception as error:
        logging.error(f"error getting user by id, error: {error}")
        raise error


def get_user_by_email(db: Session, email: str):

    try:
        """
        This function is responsible for fetching the user's information from the database on based email.

        Args:
            db (Session): Session DB
            email (str): Email

        Returns:
            UserModel
        """
        user = db.query(UserModel).filter(UserModel.email == email).first()

        return user

    except Exception as error:
        logging.error(f"error getting user by email, error: {error}")
        raise error


# POST


def create_user(db: Session, user_data_in: UserSchema):

    try:
        """
        This function is responsible for creating users in the database.

        Args:
            db (Session): Session DB
            user_data_in (UserSchema): User Data

        Returns:
            UserModel
        """

        json_data = jsonable_encoder(user_data_in)

        data_to_create = UserModel(**json_data)

        db.add(data_to_create)

        db.commit()

        db.refresh(data_to_create)

        return data_to_create

    except Exception as error:
        logging.error(f"error creating the user, error: {error.args}")
        raise error


# PUT


def update_user(db: Session, update_data: UpdateUserSchema, user_id: str):

    try:
        """
        This function is responsible for updating users in the database.

        Args:
            db (Session): Session DB
            user_data_in (UpdateUserSchema): User Data Update
            user_id (str): User ID

        Returns:
            UserModel
        """

        user_data = db.query(UserModel).filter(UserModel.user_id == user_id).first()

        update = jsonable_encoder(update_data)

        user = {k: v for k, v in update.items() if v is not None}

        for var, value in user.items():
            setattr(user_data, var, value) if value is not None else None

        db.add(user_data)
        db.commit()
        db.refresh(user_data)

        return user_data

    except Exception as error:
        logging.error(f"error updating the user, error: {error}")
        raise error
