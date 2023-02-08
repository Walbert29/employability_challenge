from sqlalchemy import TIMESTAMP, Column, Integer, String

from core.database import Base


class ApplicationModel(Base):
    """
    Application model for the  table application
    """

    __tablename__ = "application"

    application_id = Column(Integer, primary_key=True, autoincrement=True)

    user_id = Column(String(200))

    vacancy_id = Column(String(200))

    load_date = Column(TIMESTAMP(timezone=False))
