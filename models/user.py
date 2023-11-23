#!/usr/bin/python3
"""
    module containing user class
    module containing user class
"""
<<<<<<< HEAD
from os import getenv
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String
=======
from models.base_model import BaseModel, Base
>>>>>>> 04d7543e545d6bb7d68dbac502ab6e61c52e500f
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine, Column, Integer, String
from os import environ

storage_engine = environ.get("HBNB_TYPE_STORAGE")


class User(BaseModel, Base):
    """
        User class for the user
        User class for the user
    """
    if (storage_engine == 'db'):
        __tablename__ = "users"
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
<<<<<<< HEAD
        # places = relationship(
        #    'Place', backref='user', cascade='all, delete')
        # reviews = relationship(
        #    'Review', backref='user', cascade='all, delete')
=======
        places = relationship("Place", backref="user")
        reviews = relationship("Review", backref="user")
>>>>>>> 04d7543e545d6bb7d68dbac502ab6e61c52e500f
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
