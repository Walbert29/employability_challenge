import logging
from crud import user
from core.database import create_session
from fastapi import status, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from schemas.user import UserSchema, UpdateUserSchema

user_no_found = "User not found"

def get_user_by_user_id(user_id: str):
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

        return jsonable_encoder(user_data)

    except Exception as error:
        logging.error(f"services: get_user_by_user_id => {error}")
        raise HTTPException(
            status_code=status.HTTP_424_FAILED_DEPENDENCY,
            detail={"message": error.args},
        )
    finally:
        db.close()


def get_user_by_user_email(email: str):
    """
    This method is responsible for extracting all the information of a user based on his email
    """
    try:
        db = create_session()

        user_data = user.get_user_by_email(db=db, email=email)

        if user_data is None:
            return JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND,
                content={"message": user_no_found},
            )

        return jsonable_encoder(user_data)

    except Exception as error:
        logging.error(f"services: get_user_by_user_email => {error}")
        raise HTTPException(
            status_code=status.HTTP_424_FAILED_DEPENDENCY,
            detail={"message": error.args},
        )
    finally:
        db.close()


def create_user(data_user_in: UserSchema):
    """
    This method is responsible for creating a user with their respective information in the database
    """
    try:
        db = create_session()

        """
        Check if a user exists
        """

        exist_email = user.get_user_by_email(db=db, email=data_user_in.email)

        if exist_email is not None:
            return JSONResponse(
                status_code=status.HTTP_409_CONFLICT,
                content={"message": "Email already exists"},
            )

        return user.create_user(db= db, user_data_in=data_user_in)

    except Exception as error:
        db.rollback()
        logging.error(f"services: create_user => {error}")
        raise HTTPException(
            status_code=status.HTTP_424_FAILED_DEPENDENCY,
            detail={"message": error.args},
        )
    finally:
        db.close()


def update_user(user_id: str, update_data: UpdateUserSchema):
    """
    This method is responsible of update the data in database from user
    """
    try:
        db = create_session()

        """
        Check if a user exists
        """

        exist_user = user.get_user_by_id(db=db, user_id=user_id)

        if exist_user is None:
            return JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND,
                content={"message": user_no_found},
            )

        return user.update_user(db= db, update_data=update_data, user_id=user_id)

    except Exception as error:
        db.rollback()
        logging.error(f"services: update_user => {error}")
        raise HTTPException(
            status_code=status.HTTP_424_FAILED_DEPENDENCY,
            detail={"message": error.args},
        )
    finally:
        db.close()


def delete_user_by_id(user_id: str):
    """
    This method is responsible of delete a user
    """
    try:
        db = create_session()

        """
        Check if a user exists
        """

        exist_user = user.get_user_by_id(db=db, user_id=user_id)

        if exist_user is None:
            return JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND,
                content={"message": user_no_found},
            )

        user.delete_user(db= db, user_id=user_id)

        return exist_user

    except Exception as error:
        db.rollback()
        logging.error(f"services: delete_user_by_id => {error}")
        raise HTTPException(
            status_code=status.HTTP_424_FAILED_DEPENDENCY,
            detail={"message": error.args},
        )
    finally:
        db.close()
