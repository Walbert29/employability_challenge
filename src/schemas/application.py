from typing import Optional
from datetime import datetime

from pydantic import BaseModel, Field


class ApplicationSchema(BaseModel):
    """
    Application schema for create application in application table
    """

    user_id: Optional[str] = Field()

    vacancy_id: Optional[str] = Field()

    load_date: Optional[datetime] = Field(default=datetime.utcnow())