from services.employability import get_matches_by_user_id
from fastapi import APIRouter, status


employability_router = APIRouter(prefix="/employability")

# GET

@employability_router.get(
    "/user/{user_id}",
    tags=["Employability"],
    status_code=status.HTTP_200_OK,
    summary="Return vacancies that match the user",
)
def get_matches_by_user(user_id: str):
    """
    GET user by User email

    Returns:
        UserSchema
    """
    return get_matches_by_user_id(user_id=user_id)
