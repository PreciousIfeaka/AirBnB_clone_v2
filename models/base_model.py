#!/usr/bin/env python3
"""
This module contains the BaseModel class
"""
import uuid
from datetime import datetime


class BaseModel:
    """This class defines all common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """initializes instances from the dict representation"""
        if kwargs is not None:
            for key, value in kwargs.items():
                """iterates through the attributes of instance in the dict"""
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    """the datetime is converted from str to object format"""
                if key == "__class__":
                    continue
                """The class key is not added"""
                setattr(self, key, value)

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """prints the instance in the given format"""
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """updates the pulic instance attribute with the correct datetime"""
        self.updated_at = datetime.now()
        return

    def to_dict(self):
        """returns a dictionary containing all set instances"""
        new_dict = self.__dict__.copy()
        new_dict.update({'__class__': str(self.__class__.__name__)})
        new_dict["created_at"] = str(self.created_at.isoformat())
        new_dict["updated_at"] = str(self.updated_at.isoformat())
        return new_dict
