#!/usr/bin/python3
"""class definition of a State and an instance Base = declarative_base()"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City (Base):
    """Class City
    Args:
        Base (_type_): _description_
    """

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True,
                nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
