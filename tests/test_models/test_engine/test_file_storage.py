#!/usr/bin/pyhton3
""" tests for storage"""
import inspect
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import os


class TestFileStorage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.f = inspect.getmembers(FileStorage, inspect.isfunction)

    def test_save(self):
        __file_path = "file.json"
        storage.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_all(self):
        type_to_test = storage.all()
        self.assertEqual(type(type_to_test), dict)

    def test_new(self):
        d = BaseModel()
        __objects = storage.new(d)

if __name__ == '__main__':
    unittest.main()
