#!/usr/bin/python3
""" State Module for HBNB project """

from sqlalchemy import Column
# from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
import os

from models.base_model import Base
from models.base_model import BaseModel
from models.city import City


class State(BaseModel, Base):
    """ State class """

    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', cascade='delete', backref='state')

    if os.getenv('HBNB_TYPE_STORAGE') != 'db':  # FileStorage
        @property
        def cities(self):
            """getter attribute for cities

            Return:
                return the list of City instances
            """

            c_list = []
            a_list = models.storage.all(City)

            for city in a_list.values():
                if city.state_id == self.id:
                    c_list += city

            return c_list
