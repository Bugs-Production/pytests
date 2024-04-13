from api.url_facts_cat import API_CATS
from api.url_users import API_USERS
from src.schemas.cats import FactsCat
from src.schemas.users import User
from src.base_classes.response import Response
import requests


def test_get_info_cats():
    """Тестирование api о фактах кошек"""

    url = requests.get(url=API_CATS)
    response = Response(url)

    response.assert_status_code(200)
    response.validate(FactsCat)
    response.validate_count(2)


def test_get_info_user():
    """Тестирование api о юзерах"""

    url = requests.get(url=API_USERS)  # получаем ответ
    response = Response(url)

    response.assert_status_code(200)
    response.validate_count(2)
    response.validate(User)
