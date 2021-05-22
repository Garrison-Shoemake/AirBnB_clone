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
        b.save()
        self.assertNotEqual(b.created_at, b.updated_at)

if __name__ == '__main__':
    unittest.main()
