from core.database import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP

class ApplicationModel(Base):
    """
    Application model for the  table application
    """

    __tablename__ = "application"

    application_id = Column(Integer, primary_key=True, autoincrement=True)

    user_id = Column(String(200))

    vacancy_id = Column(String(200))

    load_date = Column(TIMESTAMP(timezone=False))