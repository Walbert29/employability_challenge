from core.database import Base
from sqlalchemy import Column, Integer, String
from typing import List

class Skills():
    name = Column(String(200))
    experience = Column(Integer)

class VacancyModel(Base):
    """
    User model for the  table vacancy
    """

    __tablename__ = "users"

    user_id = Column(String(200), primary_key=True)

    first_name = Column(String(200))
    
    last_name = Column(String(200))

    email = Column(String(10))

    years_previous_experience = Column(Integer)
    
    skills = List[Skills]