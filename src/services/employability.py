import logging
import numpy as np
from crud.user import get_user_by_id
from crud.vacancy import get_all_vacancies
from core.database import create_session
from fastapi import status, HTTPException
from fastapi.responses import JSONResponse

def get_matches_by_user_id(user_id: str):
    """
    This method is responsible for extracting all the information of a user based on his id
    """
    try:
        db = create_session()

        user_data = get_user_by_id(db=db, user_id=user_id)

        if user_data is None:
            return JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND,
                content={"message": "User not found"},
            )

        user_skills = (" ".join([f"{skill.get('name')} {skill.get('experience')}" for skill in user_data.skills])).lower()

        vacancies = get_all_vacancies(db=db)

        if vacancies is None:
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content={"message": "No vacancies were found that made Match"},
            )

        vacancies_to_recommend = []

        for vacancy_data in vacancies:
            vacancy_skills = (" ".join([f"{vacancy.get('name')} {vacancy.get('experience')}" for vacancy in vacancy_data.required_skills])).lower()
            similitude = get_matches(user_skills=user_skills, vacancy_skills=vacancy_skills)
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

    split_words_user_skills = user_skills.split()

    split_words_vacancy_skills = vacancy_skills.split()

    union_words_no_repeat = set(split_words_user_skills).union(set(split_words_vacancy_skills))

    matrix_zero_vacancy_skills = np.zeros(len(union_words_no_repeat))

    matrix_zero_user_skills = np.zeros(len(union_words_no_repeat))

    for i, word in enumerate(union_words_no_repeat):

        if word in split_words_user_skills:
            matrix_zero_vacancy_skills[i] = 1

        if word in split_words_vacancy_skills:
            matrix_zero_user_skills[i] = 1

    return np.dot(matrix_zero_vacancy_skills, matrix_zero_user_skills) / (np.linalg.norm(matrix_zero_vacancy_skills) * np.linalg.norm(matrix_zero_user_skills))