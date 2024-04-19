from pydantic import BaseModel, field_validator
from enum import Enum

import requests


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


def test_get_info_cats__data_validation():
    """Тестирование api о фактах кошек"""

    response = requests.get(url="https://catfact.ninja/fact")
    assert response.status_code == 200
    assert len(response.json()) == 2

    facts = response.json()
    FactsCat(**facts)


def test_get_info_user__data_validation():
    """Тестирование api о юзерах"""

    response = requests.get(url="https://gorest.co.in/public/v1/users")
    assert response.status_code == 200
    assert len(response.json()) == 2

    data = response.json()
    users = data.get("data")

    if isinstance(users, list):
        for user in users:
            User(**user)
    else:
        User(**users)
