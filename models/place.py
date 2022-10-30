#!/usr/bin/python3
"""This module has a Place subclass
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Defines the place"""

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []  # it will be the list of Amenity.id later
    amenity_ids = [""]
    amenity_ids = []  # it will be the list of Amenity.id later
