#!/usr/bin/python3
"""unittests for user instance"""
from models.user import User
import unittest

u = User()


class TestUser(unittest.TestCase):
    """test for test user"""

    def test_email(self):
        """test email"""
        self.assertTrue(isinstance(u.email, str))

    def test_password_type(self):
        """test password"""
        self.assertTrue(isinstance(u.password, str))

    def test_first_name(self):
        """test first name"""
        self.assertTrue(isinstance(u.first_name, str))

    def test_last_name(self):
        """test last name"""
        self.assertTrue(isinstance(u.last_name, str))

if __name__ == '__main__':
    unittest.main()
