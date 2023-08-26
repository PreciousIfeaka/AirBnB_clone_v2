#!/usr/bin/python3

"""This module contains the engine DBStorage and it's responsible for
   all database storage"""

from sqlalchemy import (create_engine)
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.orm import scoped_session
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """This class is responsible for all DB storage using mysqlalchemy

    Attributes:
        __engine: set to None
        __session: set to None
    """

    __engine = None
    __session: None

    classes_all = {'Amenity': Amenity, 'State': State, 'City': City,
                   'User': User, 'Review': Review, 'Place': Place}

    def __init__(self):
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}:3306/{}".
                                      format(getenv('HBNB_MYSQL_USER'),
                                             getenv('HBNB_MYSQL_PWD'),
                                             getenv('HBNB_MYSQL_HOST'),
                                             getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        # drop table if HBNB_ENV is in test environment
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        for clss in self.classes_all:
            if cls is None or cls is self.classes_all[clss] or cls is clss:
                objs = self.__session.query(self.classes_all[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)

    def new(self, obj):
        """Add obj to the current database session
        """
        if obj:
            self.__session.add(obj)

    def save(self):
        """commit all updates of the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj if not None from the current database session
        """
        if obj:
            # class name to be converted to __class__ type
            class_name = self.classes_all[type(obj).__name__]

            # to filter out the table data == obj
            obj_vals = (self.__session.query(class_name).
                        filter(class_name.id == obj.id))

            self.__session.delete(obj_vals)  # deleted the values

    def reload(self):
        """creates all tables in the database and create a session for
        the current database
        """

        Base.metadata.create_all(self.__engine)  # this creates all tables
        # create current database session
        self.__session = sessionmaker(bind=self.__engine,
                                      expire_on_commit=False)
        # making Session thread-safe
        Session = scoped_session(self.__session)
        self.__session = Session()

    def close(self):
        """close scoped_session
        """
        self.__session.close()
