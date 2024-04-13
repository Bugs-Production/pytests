from pydantic import BaseModel, Field


class FactsCat(BaseModel):
    """Валидация данных для фактов о кошек"""
    fact: str
    length: int = Field(ge=1)
