#!/usr/bin/python3
"""file contains State class"""

from os import getenv
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from models.base_model import BaseModel, Base
import models
from models.city import City


class State(BaseModel, Base):
    """This class inherits from BaseModel"""

    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if getenv("HBNB_TYPE_STORAGE") == 'db':
        # To link state objects to cities
        cities = relationship('City', cascade='all, delete, delete-orphan',
                              backref='state')
    else:
        @property
        def cities(self):
            """getter attribute that returns the list of City instances
            with state_id equal to the current State.id of the city"""
            class_dict = storage.all(City)
            class_list = []
            for city in class_dict.values():
                if City.state_id == self.id:
                    class_list.append(city)

            return class_list
