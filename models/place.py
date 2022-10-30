#!/usr/bin/python3
<<<<<<< HEAD
"""file contains Place class"""
=======
<<<<<<< HEAD
"""This module has a Place subclass
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Defines the place"""

    city_id = ""
    user_id = ""
=======
>>>>>>> 007809935c850ffb05bc675957415652752ecaa9

from models.base_model import BaseModel


class Place(BaseModel):
    """This class inherits from the BaseModel class"""
<<<<<<< HEAD
    city_id = ""    # it will be the City.id
    user_id = ""    # it will be the User.id
=======
    city_id = ""    #it will be the City.id
    user_id = ""    #it will be the User.id
>>>>>>> 80865b320f4c07f10c52f1d58b658776ca3c42fa
>>>>>>> 007809935c850ffb05bc675957415652752ecaa9
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
<<<<<<< HEAD
    amenity_ids = []  # it will be the list of Amenity.id later
=======
<<<<<<< HEAD
    amenity_ids = [""]
=======
    amenity_ids = []  #it will be the list of Amenity.id later
>>>>>>> 80865b320f4c07f10c52f1d58b658776ca3c42fa
>>>>>>> 007809935c850ffb05bc675957415652752ecaa9
