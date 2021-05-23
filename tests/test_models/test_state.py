#!/usr/bin/python3
"""testing for state instance"""
from models.state import State
import unittest

s = State()


class TestState(unittest.TestCase):
    """test for TestState"""

    def test_name(self):
        """test name"""
        self.assertTrue(isinstance(s.name, str))

if __name__ == '__main__':
    unittest.main()
