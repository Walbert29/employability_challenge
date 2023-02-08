from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, EmailStr, Field

from utils.schemas_examples import user_schema


class Skills(BaseModel):

    name: Optional[str] = Field()

    experience: Optional[int] = Field()


class UserSchema(BaseModel):
    """
    User schema for create user in users table
    """

    first_name: Optional[str] = Field()

    last_name: Optional[str] = Field()

    email: Optional[EmailStr] = Field()

    years_previous_experience: Optional[int] = Field()

    skills: Optional[List[Skills]] = Field()

    load_date: Optional[datetime] = Field(default=datetime.utcnow())

    update_date: Optional[datetime] = Field(default=datetime.utcnow())


class UpdateUserSchema(UserSchema):
    """
    User schema for update user in users table
    """

    update_date: Optional[datetime] = Field(default=datetime.utcnow())

    class Config:
        schema_extra = user_schema
