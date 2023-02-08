import logging

from fastapi import HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from src.core.database import create_session
from src.crud import user
from src.schemas.user import UpdateUserSchema, UserSchema

user_no_found = "User not found"


def get_user_by_user_id(user_id: str):
    """
    This function is responsible for searching for a user's information and returning a JSON with said data based on their id

    Args:
        user_id (str): User ID

    Returns:
        UserSchema
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
    This function is responsible for searching for a user's information and returning a JSON with said data based on their email

    Args:
        user_id (str): User ID

    Returns:
        UserSchema
    """
    try:
        db = create_session()

        # Search and verify the existence of the user

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
    This function is responsible for creating user in databse

    Args:
        data_user_in (UserSchema): User Data

    Returns:
        UserSchema
    """
    try:
        db = create_session()

        # Check if a user exists

        exist_email = user.get_user_by_email(db=db, email=data_user_in.email)

        if exist_email is not None:
            return JSONResponse(
                status_code=status.HTTP_409_CONFLICT,
                content={"message": "Email already exists"},
            )

        return user.create_user(db=db, user_data_in=data_user_in)

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
    This function is responsible for updating user in databse

    Args:
        user_id (str): User ID
        update_data (UpdateUserSchema): User Data Update

    Returns:
        UpdateUserSchema
    """
    try:
        db = create_session()

        # Check if a user exists

        exist_user = user.get_user_by_id(db=db, user_id=user_id)

        if exist_user is None:
            return JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND,
                content={"message": user_no_found},
            )

        return user.update_user(db=db, update_data=update_data, user_id=user_id)

    except Exception as error:
        db.rollback()
        logging.error(f"services: update_user => {error}")
        raise HTTPException(
            status_code=status.HTTP_424_FAILED_DEPENDENCY,
            detail={"message": error.args},
        )
    finally:
        db.close()
