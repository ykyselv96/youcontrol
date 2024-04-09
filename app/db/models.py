import uuid

from sqlalchemy import MetaData, Column, Integer, String, TIMESTAMP, ForeignKey, Table, Text
from sqlmodel import Field, SQLModel

from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func


metadata = MetaData()

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    description = Column(String, nullable=True)
    registred_at = Column(TIMESTAMP, default=func.now())


class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)

