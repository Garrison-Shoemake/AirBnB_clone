#!/usr/bin/python3
""" class called FileStorage"""
from models.base_model import BaseModel
import os
import json
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:

    """Manages file serialization"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns a dictionary"""
        return self.__objects

    def new(self, obj):
        """sets obj with obj class.id"""
        name = obj.__class__.__name__
        key = name + '.' + obj.id
        self.__objects[key] = obj

    def save(self):
        """serialize __objects to json"""
        filename = self.__file_path
        json_dict = {}
        # translate each instance to dictionary format so json can read.
        with open(filename, 'w') as objs_to_json:
            for key, value in self.__objects.items():
                json_dict[key] = value.to_dict()
            json.dump(json_dict, objs_to_json)

    def reload(self):
        """ deserialize the json file to objs"""
        filename = self.__file_path
        if os.path.exists(filename):
            with open(filename, 'r') as json_to_objs:
                tmp_dict = json.load(json_to_objs)
                for key, value in tmp_dict.items():
                    cv = value['__class__']
                    self.__objects[key] = eval('{}(**value)'.format(cv))
