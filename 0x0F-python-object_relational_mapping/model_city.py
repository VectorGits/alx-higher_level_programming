#!/usr/bin/python3
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base

class City(Base):
    """
    City class

    Attributes:
        __tablename__ (str): The name of the MySQL table to store cities.
        id (sqlalchemy.Column): The city's id. It's an auto-generated, unique integer, can’t be null and is a primary key.
        name (sqlalchemy.Column): The city's name. It's a string of 128 characters and can’t be null.
        state_id (sqlalchemy.Column): The id of the state the city belongs to. It's an integer, can’t be null and is a foreign key to states.id.
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
