from enum import Enum

from pydantic import BaseModel, ConfigDict


class Status1(Enum):
    FIRED = 'FIRED'
    TEMPORARY_NOT_WORKING = 'TEMPORARY_NOT_WORKING'
    WORKS = 'WORKS'


class Status2(Enum):
    FIRED = 'FIRED_2'
    WORKS = 'WORKS_2'


class Category(Enum):
    DRIVER = 'driver'
    COURIER = 'courier'


class BaseServiceModel(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    first_name: str
    last_name: str
    middle_name: str
    phone_number: list[str]


class Servise4Model(BaseServiceModel):
    status: Status1 = Status1.WORKS
    category: Category = Category.COURIER
    document: str = None


class Servise3Model(BaseServiceModel):
    status: Status1 = Status1.WORKS
    category: Category = Category.DRIVER
    document: str


class Servise2Model(BaseServiceModel):
    id: int = None
    status: Status2
    category: Category = Category.DRIVER
    document: str = None


class Servise1Model(BaseServiceModel):
    id: int = None
    status: Status1
    category: Category
    document: str
