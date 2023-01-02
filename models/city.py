#!/usr/bin/python3
"""file contains City class"""

from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import ForeignKey, String, Column
from sqlalchemy.orm import relationship
from models.place import Place


class City(BaseModel, Base):
    """This class inherits from the BaseModel class"""
    __tablename__ = "cities"
    state_id = Column(String(60), ForeignKey("states_id"), nullable=False)
    name = Column(String(128), nullable=False)
    places = relationship('Place', cascade='all, delete, delete-orphan',
                          backref='cities')
