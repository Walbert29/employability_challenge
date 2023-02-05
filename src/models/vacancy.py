from core.database import Base
from sqlalchemy import Column, Integer, String
from typing import List

class RequiredSkills():
    name = Column(String(200))
    experience = Column(Integer)

class VacancyModel(Base):
    """
    User model for the  table vacancy
    """

    __tablename__ = "vacancy"

    vacancy_id = Column(String(200), primary_key=True)

    position_name = Column(String(200))
    
    company_name = Column(String(200))

    salary = Column(Integer)

    currency = Column(String(3))
    
    required_skills = List[RequiredSkills]