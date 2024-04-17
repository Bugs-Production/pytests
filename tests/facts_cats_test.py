from urls.urls import API_CATS, API_USERS
from tests.schemas.schema import FactsCat, User
import requests


def test_get_info_cats():
    """Тестирование api о фактах кошек"""

    response = requests.get(url=API_CATS)
    assert response.status_code == 200
    assert len(response.json()) == 2

    facts = response.json()
    if isinstance(facts, list):
        for fact in facts:
            FactsCat(**fact)
    else:
        FactsCat(**facts)


def test_get_info_user():
    """Тестирование api о юзерах"""

    response = requests.get(url=API_USERS)
    assert response.status_code == 200
    assert len(response.json()) == 2

    data = response.json()
    users = data.get("data")

    if isinstance(users, list):
        for user in users:
            User(**user)
    else:
        User(**users)
