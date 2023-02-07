from typing import List, Optional
from datetime import datetime

from pydantic import BaseModel, Field

class Skills(BaseModel):

    name: Optional[str] = Field()

    experience: Optional[int] = Field()


class VacancySchema(BaseModel):
    """
    Vacancy schema for create vacancy in vacancy table
    """

    vacancy_link: Optional[str] = Field()

    position_name: Optional[str] = Field()

    company_name: Optional[str] = Field()

    salary: Optional[int] = Field()

    currency: Optional[str] = Field()

    required_skills: Optional[List[Skills]] = Field()

    load_date: Optional[datetime] = Field(default=datetime.utcnow())