import enum
import os

from dotenv import load_dotenv
from sqlalchemy import (
    MetaData, Table, Column, Integer, String, Enum, URL, create_engine
)
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.ext.asyncio import create_async_engine
from pydantic import BaseModel


load_dotenv()

metadata_obj = MetaData()

url_object = URL.create(
    "postgresql+psycopg",
    username=os.getenv('USERNAME'),
    password=os.getenv('PASSWORD'),
    host=os.getenv('HOST'),
    database=os.getenv('DATABASE'),
)


class Status(enum.Enum):
    FIRED = 1
    TEMPORARY_NOT_WORKING = 2
    WORKS = 3


class Category(enum.Enum):
    DRIVER = 1
    COURIER = 2


user = Table(
    "user",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("first_name", String(50), nullable=False),
    Column("last_name", String(50), nullable=False),
    Column("middle_name", String(50), nullable=False),
    Column("phone_number", ARRAY(String(20))),
    Column("status", Enum(Status)),
    Column("category", Enum(Category)),
    Column("document", String(20)),
)


class DataHandler:
    def __init__(self, instance: BaseModel, table: Table = user) -> None:
        self._instance = instance
        self._table = table

    @property
    def instance(self) -> BaseModel:
        return self._instance

    @instance.setter
    def instance(self, instance: BaseModel) -> None:
        self._instance = instance

    @property
    def table(self) -> Table:
        return self._table

    @table.setter
    def table(self, table: Table) -> None:
        self._table = table

    def create(self) -> None:
        data = self._instance.model_dump()
        self._table.insert().values(data)

    def update(self) -> None:
        self._table.update().where(
            self._table.c.id==self._instance.id).values(
                self._instance.model_dump())


async def create_a_engine():
    asyncio_engine = create_async_engine(url_object, echo=True)
    async with asyncio_engine.connect() as connection:
        yield connection


if __name__ == '__main__':
    engine = create_engine(url_object, echo=True)
    metadata_obj.create_all(engine)
