#!/usr/bin/python3
"""file contains Review class
"""

from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
import models


class Review(BaseModel, Base):
    """This class inherits from the BaseModel class
    """

    __tablename__ = 'reviews'

    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    text = Column(String(1024), nullable=False)
