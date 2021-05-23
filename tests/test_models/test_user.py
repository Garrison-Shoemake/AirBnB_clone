#!/usr/bin/python3
from models.user import User
import unittest

u = User()

class TestUser(unittest.TestCase):

    def test_email(self):
        self.assertTrue(type(u.email) is str)

    def test_password_type(self):
        self.assertTrue(type(u.password) is str)

    def test_first_name(self):
        self.assertTrue(type(u.first_name) is str)

    def test_last_name(self):
        self.assertTrue(type(u.last_name) is str)

if __name__ == '__main__':
    unittest.main()
