#!/usr/bin/pyhton3
""" tests for storage"""
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os


class TestFileStorage(unittest.TestCase):

    def test_save(self):
        b = BaseModel()
        f = FileStorage()
        b.save()
        self.assertNotEqual(b.created_at, b.updated_at)

    def test_all(self):
        b = FileStorage()
        type_to_test = b.all()
        self.assertEqual(type(type_to_test), dict)

    def test_new(self):
        b = FileStorage()
        d = BaseModel()
        user = b.new(d)

    def test_save_file(self):
        b = FileStorage()
        f = b.save()
        self.assertTrue(os.path.exists('file.json'))


if __name__ == '__main__':
    unittest.main()
