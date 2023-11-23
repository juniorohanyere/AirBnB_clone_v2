#!/usr/bin/python3
<<<<<<< HEAD
""" City Module for HBNB project """

from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import ForeignKey

from models.base_model import Base
from models.base_model import BaseModel


class City(BaseModel, Base):
    """ The city class, contains state ID and name """

    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
=======
"""
    contains City class to represent a city
    contains City class to represent a city
"""

from models.base_model import BaseModel, Base
from models.state import State
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey
from os import environ

storage_engine = environ.get("HBNB_TYPE_STORAGE")


class City(BaseModel, Base):
    """ City class :City class to represent a city
    City class :City class to represent a city"""

    if (storage_engine == "db"):
        __tablename__ = "cities"
        state_id = Column(String(60), ForeignKey(State.id))
        name = Column(String(128), nullable=False)
        places = relationship("Place", backref="cities")
    else:
        name = ""
        state_id = ""
>>>>>>> 04d7543e545d6bb7d68dbac502ab6e61c52e500f
