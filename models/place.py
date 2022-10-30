#!/usr/bin/python3
<<<<<<< HEAD
"""This module has a Place subclass
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Defines the place"""

    city_id = ""
    user_id = ""
=======

from models.base_model import BaseModel

class Place(BaseModel):
    """This class inherits from the BaseModel class"""
    city_id = ""    #it will be the City.id
    user_id = ""    #it will be the User.id
>>>>>>> 80865b320f4c07f10c52f1d58b658776ca3c42fa
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
<<<<<<< HEAD
    amenity_ids = [""]
=======
    amenity_ids = []  #it will be the list of Amenity.id later
>>>>>>> 80865b320f4c07f10c52f1d58b658776ca3c42fa
