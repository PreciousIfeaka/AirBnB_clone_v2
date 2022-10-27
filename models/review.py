#!/usr/bin/python3

from models.base_model import BaseModel

class Review(BaseModel):
    """This class inherits from the BaseModel class"""
    place_id = ""   #it will be the Place.id
    user_id = ""    #it will be the User.id
    text = ""
