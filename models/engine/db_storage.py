#!/usr/bin/python3
"""new engine DBStorage
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
import os

from models.base_model import Base
from models.base_model import BaseModel
from models.city import City
from models.state import State
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review


classes = {
    'BaseModel': BaseModel, 'User': User, 'Place': Place, 'State': State,
    'City': City, 'Amenity': Amenity, 'Review': Review
}


class DBStorage:
    """database storage class
    """

    __engine = None
    __session = None

    def __init__(self):
        """initialise self
        """

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(os.getenv('HBNB_MYSQL_USER'),
                                              os.getenv('HBNB_MYSQL_PWD'),
                                              os.getenv('HBNB_MYSQL_HOST'),
                                              os.getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)

        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query all objects depending on a specific class name

        Args:
            cls: the class name to query the objects from

        Return:
            return a dictionary
        """

        dictionary = {}

        for key in classes.keys():
            if cls is None or cls == classes[key] or cls == key:
                objs = self.__session.query(classes[key]).all()
                for obj in objs:
                    k = obj.__class__.__name__ + '.' + obj.id
                    dictionary[key] = obj

        return dictionary

    def new(self, obj):
        """adds an object to the current database session

        Args:
            obj: object to add to the database session

        Return:
            return nothing
        """

        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session

        Return:
            return nothing
        """

        self.__session.commit()

    def delete(self, obj=None):
        """deletes an object from the current database session

        Args:
            obj (optional): the object to delete

        Return:
            return nothing
        """

        if obj is not None:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        """creates current database session

        Return:
            return nothing
        """

        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        cur_session = scoped_session(session)
        self.__session = cur_session()
