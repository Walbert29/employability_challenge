import uuid
from core.database import Base
from sqlalchemy import Column, Integer, String, JSON, ARRAY, TIMESTAMP

class VacancyModel(Base):
    """
    Vacancy model for the  table vacancy
    """

    __tablename__ = "vacancy"

    vacancy_id = Column(String(200), primary_key=True, default=str(uuid.uuid4()))

    vacancy_link = Column(String(200))

    position_name = Column(String(200))

    company_name = Column(String(200))

    salary = Column(Integer)

    currency = Column(String(3))

    required_skills = Column(ARRAY(JSON))

    load_date = Column(TIMESTAMP(timezone=False))