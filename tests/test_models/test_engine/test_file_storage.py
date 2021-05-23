#!/usr/bin/pyhton3
""" tests for storage"""
import inspect
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import os
import json


class TestFileStorage(unittest.TestCase):
    """tests for file storage"""

    @classmethod
    def setUpClass(cls):
        cls.f = inspect.getmembers(FileStorage, inspect.isfunction)

    def test_save(self):
        f = FileStorage()
        if os.path.exists(f._FileStorage__file_path):
            os.remove(f._FileStorage__file_path)
        b = BaseModel()
        b.save()
        with open('file.json') as jf:
            tmp = json.load(jf)
        self.assertTrue(type(tmp) is dict)

    def test_all(self):
        type_to_test = storage.all()
        self.assertIsNotNone(type_to_test)
        self.assertIsInstance(storage.all(), dict)

    def test_new(self):
        f = FileStorage()
        tmp = f.all().copy()
        BaseModel()
        self.assertFalse(tmp == f.all())

    def test_reload(self):
        BaseModel()
        obj = storage.all()
        storage.reload()
        obj_reloaded = storage.all()
        self.assertEqual(obj, obj_reloaded)

    def test_reload2(self):
        f = FileStorage()
        b = BaseModel()
        b.save()
        f.reload()
        test_reload = f.all().copy()
        b.my_num = 32
        self.assertEqual(b.my_num, 32)
        f.reload()
        self.assertNotEqual(f.all(), test_reload)
if __name__ == '__main__':
    unittest.main()
