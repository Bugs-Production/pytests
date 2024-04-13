"""Вспомогательные сообщения при ложных тестах"""

from enum import Enum


class GlobalErrorMessages(Enum):
    WRONG_STATUS_CODE = "The server returned an unexpected status code. Expected {}, but got {}."
    WRONG_ELEMENT_COUNT = "The count of elements is incorrect. Expected {} elements, but got {}."
