#!/c/msys64/mingw64/bin/python

from models.base_model import BaseModel

class City(BaseModel):
    """This class inherits from the BaseModel class"""
    state_id = ""
    name = ""
