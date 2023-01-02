#!/usr/bin/python3
"""file contains Amenity class
"""

from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from models.place import place_amenity


class Amenity(BaseModel, Base):
    """This class also inherits from the BaseModel class
    """

    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)

    place_amenities = relationship('Place', secondary=place_amenity)
