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
        f = FileStorage()
        if os.path.exists(f._FileStorage__file_path):
            os.remove(f._FileStorage__file_path)
        b = BaseModel()
        storage.save()
        self.assertTrue(os.path.exists(f._FileStorage__file_path))

    def test_all(self):
        type_to_test = storage.all()
        self.assertIsNotNone(type_to_test)
        self.assertIsInstance(storage.all(), dict)

    def test_new(self):
        d = BaseModel()
        __objects = storage.new(d)

    def test_reload(self):
        f = FileStorage()
        if os.path.exists(f._FileStorage__file_path):
            os.remove(f._FileStorage__file_path)
        f1 = FileStorage()
        f2 = FileStorage()
        f2.save()
        f2.reload()
        testreload = f2.all()
        self.assertEqual(testreload, f1.all())

if __name__ == '__main__':
    unittest.main()
