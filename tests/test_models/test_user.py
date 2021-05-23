#!/usr/bin/python3
"""unittests for user instance"""
from models.user import User
import unittest

u = User()


class TestUser(unittest.TestCase):

    """test for test user"""

    def test_email(self):
        self.assertTrue(isinstance(u.email, str))

    def test_password_type(self):
        self.assertTrue(isinstance(u.password, str))

    def test_first_name(self):
        self.assertTrue(isinstance(u.first_name, str))

    def test_last_name(self):
        self.assertTrue(isinstance(u.last_name, str))

if __name__ == '__main__':
    unittest.main()
