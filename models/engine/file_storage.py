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
        name = obj.__class__.__name__i
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

        # if os.path.exists(filename):
        try:
            with open(filename, 'r', encoding='utf-8') as json_to_objs:
                tmp_dict = json.load(json_to_objs)
        # loop through json file, update object at that key to the class args
                for key, value in tmp_dict.items():
                    self.__objects[key] = BaseModel(**value)
        except:
            pass
