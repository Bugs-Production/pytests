"""Enum для юзеров"""

from enum import Enum


class Gender(Enum):
    female = "female"
    male = "male"


class Status(Enum):
    active = "active"
    inactive = "inactive"
