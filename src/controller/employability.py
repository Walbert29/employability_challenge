from services.employability import get_matches_by_user_id
from fastapi import APIRouter, status


employability_router = APIRouter(prefix="/employability")

# GET

@employability_router.get(
    "/user/{user_id}",
    tags=["Employability"],
    status_code=status.HTTP_200_OK,
    summary="Return the vacancies to which a person can apply",
)
def get_matches_by_user(user_id: str):
    """
    This controller is in charge of returning the vacancies to which people can apply

    Method:
        GET

    Args:
        user_id (str): User ID

    Returns:
        List[EmployabilitySchema]
    """
    return get_matches_by_user_id(user_id=user_id)
