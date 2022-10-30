#!/usr/bin/python3
"""This module contains the Review subclass
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """This class defines the reviews"""

    place_id = ""
    user_id = ""
    text = ""
