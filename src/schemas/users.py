from pydantic import BaseModel, field_validator
from src.enums.user_enums import Gender, Status


class User(BaseModel):
    """Валидация данных юзеров"""
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
