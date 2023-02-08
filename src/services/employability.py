import logging

import numpy as np
from fastapi import HTTPException, status
from fastapi.responses import JSONResponse

from src.core.database import create_session
from src.crud.user import get_user_by_id
from src.crud.vacancy import get_all_vacancies


def get_matches_by_user_id(user_id: str):
    """
    This function is responsible for searching for vacancies that fit the user's profile

    Args:
        user_id (str): User ID

    Returns:
        List[VacancySchema]
    """
    try:
        db = create_session()

        # Search and verify the existence of the user

        user_data = get_user_by_id(db=db, user_id=user_id)

        if user_data is None:
            return JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND,
                content={"message": "User not found"},
            )

        # Match the skills described in the user's profile

        user_skills = (
            " ".join(
                [
                    f"{skill.get('name')} {skill.get('experience')}"
                    for skill in user_data.skills
                ]
            )
        ).lower()

        # Check if there are vacancies in the database to generate the matches

        vacancies = get_all_vacancies(db=db)

        if vacancies is None:
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content={"message": "No vacancies were found that made Match"},
            )

        vacancies_to_recommend = []

        for vacancy_data in vacancies:

            # Match the skills required in the vacancy

            vacancy_skills = (
                " ".join(
                    [
                        f"{vacancy.get('name')} {vacancy.get('experience')}"
                        for vacancy in vacancy_data.required_skills
                    ]
                )
            ).lower()

            # Send the function the list of the required skills and the achieved skills of the user

            similitude = get_matches(
                user_skills=user_skills, vacancy_skills=vacancy_skills
            )

            # Check at least 50% similarity

            if similitude >= 0.5:
                vacancies_to_recommend.append(vacancy_data)

        if vacancies_to_recommend == []:
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content={"message": "No vacancies were found that made Match"},
            )

        return vacancies_to_recommend

    except Exception as error:
        logging.error(f"services: get_matches_by_user_id => {error}")
        raise HTTPException(
            status_code=status.HTTP_424_FAILED_DEPENDENCY,
            detail={"message": error.args},
        )
    finally:
        db.close()


def get_matches(user_skills: str, vacancy_skills: str):

    # Split the skills of the requisition and the user by words, and eliminate duplicates

    split_words_user_skills = user_skills.split()

    split_words_vacancy_skills = vacancy_skills.split()

    union_words_no_repeat = set(split_words_user_skills).union(
        set(split_words_vacancy_skills)
    )

    # Create matrix of 0 the size of the split words

    matrix_zero_vacancy_skills = np.zeros(len(union_words_no_repeat))

    matrix_zero_user_skills = np.zeros(len(union_words_no_repeat))

    # Modify the value of the array to 1 in case the word matches the skill

    for index, word in enumerate(union_words_no_repeat):

        if word in split_words_user_skills:
            matrix_zero_vacancy_skills[index] = 1

        if word in split_words_vacancy_skills:
            matrix_zero_user_skills[index] = 1

    # The product between the matrices is realized

    return np.dot(matrix_zero_vacancy_skills, matrix_zero_user_skills) / (
        np.linalg.norm(matrix_zero_vacancy_skills)
        * np.linalg.norm(matrix_zero_user_skills)
    )
