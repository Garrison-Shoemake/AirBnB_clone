#!/usr/bin/python3
""" class called FileStorage"""
from models.base_model import BaseModel
import os
import json


class FileStorage:

    """Manages file serialization"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns a dictionary"""
        return self.__objects

    def new(self, obj):
        """sets obj with obj class.id"""
        key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[key] = obj

    def save(self):
        """serialize __objects to json"""
        filename = self.__file_path
        json_dict = {}

        with open(filename, 'w') as objs_to_json:
            json_dict = self.__objects
            objs_to_json.write(json.dumps(json_dict, indent=2))

    def reload(self):
        """ deserialize the json file to objs"""
        filename = self.__file_path

        if os.path.exists(filename):
            with open(filename, 'r') as json_to_objs:
                self.__objects = json.loads(json_to_objs)
