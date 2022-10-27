#!/c/msys64/mingw64/bin/python
import uuid
from datetime import datetime, time, date
import models

class BaseModel():
    '''This class defines all common attributes/methods for other classes'''

    def __init__(self, *args, **kwargs):
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
