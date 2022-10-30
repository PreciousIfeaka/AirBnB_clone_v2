<<<<<<< HEAD
#!/usr/bin/env python3
"""This module stores all instances of the class"""

from models.base_model import BaseModel
import json
=======
#!/usr/bin/python3
"""file contains FileStorage class"""

import os
import json
from models.base_model import BaseModel
>>>>>>> 80865b320f4c07f10c52f1d58b658776ca3c42fa
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

<<<<<<< HEAD

=======
<<<<<<< HEAD

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
=======
>>>>>>> 007809935c850ffb05bc675957415652752ecaa9
class FileStorage:
    '''This class serializes instances to a JSON file and deserializes
    JSON file to instances'''
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        '''This function returns the dictionary __objects'''
        return self.__objects

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
>>>>>>> 80865b320f4c07f10c52f1d58b658776ca3c42fa
