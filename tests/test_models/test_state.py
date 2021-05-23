#!/usr/python3
from models.state import State
import unittest

s = State()

class TestState(unittest.TestCase):

    def test_name(self):
        self.assertTrue(type(s.name) is str)

if __name__ == '__main__':
    unittest.main()
