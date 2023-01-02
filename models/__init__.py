#!/usr/bin/python3
"""creates unique FileStorage instance for application"""


from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from os import getenv
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage


if getenv('HBNB_TYPE_STORAGE') == 'db':
    storage = DBStorage()
    storage.reload()
else:
    storage = FileStorage()
    storage.reload()
