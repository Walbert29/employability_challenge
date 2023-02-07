import logging
from models.user import UserModel
from schemas.user import UserSchema, UpdateUserSchema
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder


# GET

def get_user_by_id(db: Session, user_id: str):

    try:
        """
        GET a user's information based on their ID
        """
        user = db.query(UserModel).filter(UserModel.user_id == user_id).first()

        return user

    except Exception as error:
        logging.error(f"error getting user by id, error: {error}")
        raise error


def get_user_by_email(db: Session, email: str):

    try:
        """
        GET a user's information based on email
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
        POST for create a user
        """

        json_data = jsonable_encoder(user_data_in)

        data_to_create = UserModel(**json_data)

        db.add(data_to_create)

        db.commit()

        db.refresh(data_to_create)

        return user_data_in

    except Exception as error:
        logging.error(f"error creating the user, error: {error.args}")
        raise error


# PUT


def update_user(db: Session, update_data: UpdateUserSchema, user_id: str):

    try:
        """
        POST for create a user
        """

        user_data = db.query(UserModel).filter(UserModel.user_id == user_id).first()

        update = jsonable_encoder(update_data)

        user = {k: v for k, v in update.items() if v is not None}

        for var, value in user.items():
            setattr(user_data, var, value) if value is not None else None

        db.add(user_data)
        
        return update

    except Exception as error:
        logging.error(f"error updating the user, error: {error}")
        raise error


# DELETE

def delete_user(db: Session, user_id: str):
    try:
        """
        DELETE user of database
        """
        user = db.query(UserModel).filter(UserModel.user_id == user_id).first()

        if user is None:
            return None

        db.query(UserModel).filter(UserModel.user_id == user_id).delete()

        db.commit()

        return user

    except Exception as error:
        logging.error(f"error deleting the user, error: {error}")
        raise error
