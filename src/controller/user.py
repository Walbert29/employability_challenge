from fastapi import APIRouter, status

from src.schemas.user import UpdateUserSchema, UserSchema
from src.services import user

user_router = APIRouter(prefix="/user")

# GET


@user_router.get(
    "/email/{email}",
    tags=["User"],
    status_code=status.HTTP_200_OK,
    summary="Return the information of a user based on his email",
)
def get_user_by_email(email: str):
    """
    This controller is responsible for returning the information stored in a user's database, based on their email

    Method:
        GET

    Args:
        email (str): Email

    Returns:
        UserSchema
    """
    return user.get_user_by_user_email(email=email)


@user_router.get(
    "/{user_id}",
    tags=["User"],
    status_code=status.HTTP_200_OK,
    summary="Return the information of a user based on his id",
)
def get_user_by_id(user_id: str):
    """
    This controller is responsible for returning the information stored in a user's database, based on their id

    Method:
        GET

    Args:
        user_id (str): user ID

    Returns:
        UserSchema
    """
    return user.get_user_by_user_id(user_id=user_id)


# POST


@user_router.post(
    "/create",
    tags=["User"],
    status_code=status.HTTP_201_CREATED,
    summary="Create an user in the database",
)
def create_user(data_user: UserSchema):
    """
    This controller is responsible for making the request for the creation of a user in the database

    Method:
        POST

    Args:
        data_user (UserSchema): User Data

    Returns:
        UserSchema
    """
    return user.create_user(data_user_in=data_user)


# PUT


@user_router.put(
    "/update/{user_id}",
    tags=["User"],
    status_code=status.HTTP_200_OK,
    summary="Update data from user",
)
def update_user(user_id: str, data_user: UpdateUserSchema):
    """
    This controller is responsible for making the request for the update data of a user in the database

    Method:
        PUT

    Args:
        user_id (str): User ID
        data_user (UpdateUserSchema): User Data Update

    Returns:
        UserSchema
    """
    return user.update_user(user_id=user_id, update_data=data_user)
