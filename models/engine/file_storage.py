#!/usr/bin/python3
"""This module stores all instances of the class"""

import os
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    '''This class serializes instances to a JSON file and deserializes
    JSON file to instances'''
    __file_path = 'file.json'
    __objects = {}

    classes = {
                "User": User, "Place": Place, "State": State,
                "City": City, "Amenity": Amenity, "Review": Review,
                "Review": Review
              }

    def all(self, cls=None):
        '''This function returns the dictionary __objects'''
        if cls:
            if cls.__name__ in self.classes:
                temp_dict = {}
                for key, value in self.__objects.items():
                    if key.split(".")[0] == cls.__name__:
                        temp_dict[key] = value
            else:
                raise NameError()
        else:
            temp_dict = self.__objects

        return temp_dict

    def new(self, obj):
        '''sets in __objects the obj with key <obj class name>.id'''
        self.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self):
        '''serializes __objects to the JSON file (path: __file_path)'''
        with open(self.__file_path, 'w') as file:
            dic_t = {k: v.to_dict() for k, v in self.__objects.items()}
            json.dump(dic_t, file)

    def reload(self):
        '''deserializes the JSON file to __objects (only if the JSON
        file (__file_path) exists ; otherwise, do nothing. If the file
        doesn’t exist, no exception should be raised)'''
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, 'r') as file:
                dic_t = json.loads(file.read())
                for k, v in dic_t.items():
                    self.__objects[k] = eval(k.split(".")[0])(**v)

    def delete(self, obj=None):
        """Deletes obj from __objects if it is inside.
        The method should not do anything if obj is None"""
        if obj:
            """The key is converted to the format with which it is stored
            in __objects"""
            key = "{}.{}".format(type(obj).__name__, obj.id)
            if key in self.__objects:
                del self.__objects[key]
