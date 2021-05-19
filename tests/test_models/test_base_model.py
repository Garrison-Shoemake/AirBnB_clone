#!/usr/bin/python3
""" this is the unittest file for the AirBnB project """


import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBase(unittest.TestCase):
    """ These tests will be conducted on the base_model class """

    def test_self_id(self):
        """ this method tests BaseModel's save() method """
        b1 = BaseModel()
        b1.save()
        self.assertNotEqual(b1.created_at, b1.updated_at)

    def test_save(self):
        model = BaseModel()
        time1 = model.updated_at
        model.save()
        time2 = model.updated_at
        self.assertNotEqual(time1, time2)


if __name__ == '__main__':
    unittest.main()
