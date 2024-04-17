from pydantic import BaseModel, field_validator
from enum import Enum


class FactsCat(BaseModel):
    fact: str
    length: int


class Gender(Enum):
    female = "female"
    male = "male"


class Status(Enum):
    active = "active"
    inactive = "inactive"


class User(BaseModel):
    id: int
    name: str
    email: str
    gender: Gender
    status: Status

    @field_validator("email")
    def validate_email(cls, email):
        if not "@" in email:
            raise ValueError("ValueError: Email must contain the '@' symbol")
        return email
