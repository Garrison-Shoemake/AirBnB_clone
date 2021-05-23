#!/usr/bin/python3
""" this is the unittest file for the AirBnB project """

import os
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestBase(unittest.TestCase):
    """ These tests will be conducted on the base_model class """

    def test_self_id(self):
        """ this method tests BaseModel's save() method """
        b1 = BaseModel()
        b1.save()
        self.assertNotEqual(b1.created_at, b1.updated_at)

    def test_save(self):
        """test for saving"""
        model = BaseModel()
        time1 = model.updated_at
        model.save()
        time2 = model.updated_at
        self.assertNotEqual(time1, time2)

    def test_dict(self):
        """test for dict"""
        b1 = BaseModel()
        b1d = b1.to_dict()
        self.assertIn("__class__", b1d.keys())

    def test_str(self):
        """test for str"""
        b = BaseModel()
        self.assertEqual(b.__str__(), "[BaseModel] ({}) {}".
                         format(b.id, b.__dict__))

    def test_save(self):
        """test for save"""
        b = BaseModel()
        b.save()
        self.assertNotEqual(b.created_at, b.updated_at)

    def test_save_file(self):
        """test for savefile"""
        b = FileStorage()
        f = b.save()
        self.assertTrue(os.path.exists('file.json'))

if __name__ == '__main__':
    unittest.main()
