#!/usr/bin/python3
"""file contains User class
"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.place import Place
from models.review import Review
from sqlalchemy.ext.declarative import declarative_base

class User(BaseModel, Base):
    """class User that inherits from BaseModel
    """

    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)

    places = relationship('Place', cascade='all, delete, delete-orphan',
                          backref='user')
    reviews = relationship('Review', cascade='all, delete, delete-orphan',
                           backref='user')
