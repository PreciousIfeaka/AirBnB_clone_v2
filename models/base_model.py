#!/usr/bin/python3
<<<<<<< HEAD
"""
This module contains the BaseModel class
"""
import uuid
from datetime import datetime
import models
=======
>>>>>>> 80865b320f4c07f10c52f1d58b658776ca3c42fa

import uuid
from datetime import datetime, time, date
import models

class BaseModel():
    '''This class defines all common attributes/methods for other classes'''

    def __init__(self, *args, **kwargs):
<<<<<<< HEAD
        """initializes instances from the dict representation"""
        if kwargs:
            for key, value in kwargs.items():
                """iterates through the attributes of instance in the dict"""
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    """the datetime is converted from str to object format"""
                if key == "__class__":
                    continue
                """The class key is not added"""
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
=======
        if kwargs:
            for k, v in kwargs.items():
                if k == 'created_at' or k == 'updated_at':
                    v = datetime.strptime(v, '%Y-%m-%dT%H:%M:%S.%f')
                if k == '__class__':
                    continue
                setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.today()
>>>>>>> 80865b320f4c07f10c52f1d58b658776ca3c42fa
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__,
                self.id, self.__dict__)

    def save(self):
        '''updates the public instance attribute updated_at with the
        current datetime
        '''
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        '''returns a dictionary containing all keys/values of __dict__
        of the instance'''
        new_dict = self.__dict__.copy()
        new_dict.update({'__class__': __class__.__name__})
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
