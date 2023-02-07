from services import user
from schemas.user import UserSchema, UpdateUserSchema
from fastapi import APIRouter, status


user_router = APIRouter(prefix="/user")

# GET

@user_router.get(
    "/email/{email}",
    tags=["User"],
    status_code=status.HTTP_200_OK,
    summary="Return a user by email",
)
def get_user_by_email(email: str):
    """
    GET user by User email

    Returns:
        UserSchema
    """
    return user.get_user_by_user_email(email=email)


@user_router.get(
    "/{user_id}",
    tags=["User"],
    status_code=status.HTTP_200_OK,
    summary="Return a user by id",
)
def get_user_by_id(user_id: str):
    """
    GET user by User ID

    Returns:
        UserSchema
    """
    return user.get_user_by_user_id(user_id=user_id)


# POST

@user_router.post(
    "/create",
    tags=["User"],
    status_code=status.HTTP_201_CREATED,
    summary="Create an user",
)
def create_user(data_user: UserSchema):
    """
    CREATE an user in database

    Returns:
        UserSchema
    """
    return user.create_user(data_user_in=data_user)


# PUT

@user_router.put(
    "/update/{user_id}",
    tags=["User"],
    status_code=status.HTTP_200_OK,
    summary="Create an user",
)
def update_user(user_id:str, data_user: UpdateUserSchema):
    """
    UPDATE data from user in database

    Returns:
        UserSchema
    """
    return user.update_user(user_id=user_id, update_data=data_user)


# DELETE

@user_router.delete(
    "/delete/{user_id}",
    tags=["User"],
    status_code=status.HTTP_200_OK,
    summary="Delete an user",
)
def delete_user(user_id:str):
    """
    DELETE user from database

    Returns:
        UserSchema
    """
    return user.delete_user_by_id(user_id=user_id)
