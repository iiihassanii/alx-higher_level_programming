#!/usr/bin/python3
"""class definition of a State and an instance Base = declarative_base()"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.orm import declarative_base


Base = declarative_base(metadata=MetaData())


class State (Base):
    """Class State
    Args:
        Base (_type_): _description_
    """

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True,
                nullable=False, unique=True)
    name = Column(String(128), nullable=False)
