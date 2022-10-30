#!/usr/bin/env python3
"""This module stores all instances of the class"""

from models.base_model import BaseModel
import json
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """This class stores all instances to a json file"""
    """and deserializes json file to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        with open(self.__file_path, 'w+', encoding="utf-8") as f:
            json.dump({key: value.to_dict()
                      for key, value in self.__objects.items()}, f)

    def reload(self):
        try:
            with open(self.__file_path, 'r', encoding="utf-8") as f:
                new_dict = json.load(f)
                for key, value in new_dict.items():
                    self.__objects[key] = eval(key.split(".")[0])(**value)
                    """This line create an instance from the decoded dict"""
        except Exception:
            pass
