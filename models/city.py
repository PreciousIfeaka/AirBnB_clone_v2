#!/usr/bin/python3
"""file contains City class"""

from models.base_model import BaseModel, Base
from sqlalchemy import ForeignKey, String, Column


class City(BaseModel, Base):
    """This class inherits from the BaseModel class"""
    __tablename__ = "cities"
    state_id = Column(String(60), ForeignKey("states_id"))
    name = Column(String(128), nullable=False)
