#!/usr/bin/python3
""" Base model defines all attributes for other classes"""
from datetime import datetime
import uuid



class BaseModel:
    """ Public instance of id, created_at, updated_at"""

    def __init__(self, *args, **kwargs):

        if kwargs:
            for key, value in kwargs.items():
                if key is ('created_at', 'updated_at'):
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key is not ('__class__'):
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        c = self.__class__.__name__
        i = self.id
        d = self.__dict__
        return "[{}] ({}) {}".format(c, i, d)

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        dict_to_return = dict(self.__dict__)
        dict_to_return['__class__'] = self.__class__.__name__
        dict_to_return['created_at'] = self.created_at.isoformat()
        dict_to_return['updated_at'] = self.updated_at.isoformat()

        return dict_to_return
