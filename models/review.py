#!/usr/bin/python3
<<<<<<< HEAD
"""file contains Review class"""
=======
<<<<<<< HEAD
"""This module contains the Review subclass
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """This class defines the reviews"""

    place_id = ""
    user_id = ""
=======
>>>>>>> 007809935c850ffb05bc675957415652752ecaa9

from models.base_model import BaseModel


class Review(BaseModel):
    """This class inherits from the BaseModel class"""
<<<<<<< HEAD
    place_id = ""   # it will be the Place.id
    user_id = ""    # it will be the User.id
=======
    place_id = ""   #it will be the Place.id
    user_id = ""    #it will be the User.id
>>>>>>> 80865b320f4c07f10c52f1d58b658776ca3c42fa
>>>>>>> 007809935c850ffb05bc675957415652752ecaa9
    text = ""
