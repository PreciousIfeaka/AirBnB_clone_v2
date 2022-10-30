#!/usr/bin/python3
<<<<<<< HEAD
"""This module contains the Review subclass
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """This class defines the reviews"""

    place_id = ""
    user_id = ""
=======

from models.base_model import BaseModel

class Review(BaseModel):
    """This class inherits from the BaseModel class"""
    place_id = ""   #it will be the Place.id
    user_id = ""    #it will be the User.id
>>>>>>> 80865b320f4c07f10c52f1d58b658776ca3c42fa
    text = ""
