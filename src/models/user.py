import uuid

from sqlalchemy import ARRAY, JSON, TIMESTAMP, Column, Integer, String

from src.core.database import Base


class UserModel(Base):
    """
    User model for the table Users
    """

    __tablename__ = "users"

    user_id = Column(String(200), primary_key=True, default=str(uuid.uuid4()))

    first_name = Column(String(200))

    last_name = Column(String(200))

    email = Column(String(10))

    years_previous_experience = Column(Integer)

    skills = Column(ARRAY(JSON))

    load_date = Column(TIMESTAMP(timezone=False))

    update_date = Column(TIMESTAMP(timezone=False))
