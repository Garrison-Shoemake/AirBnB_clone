#!/usr/bin/python3
""" This is the unittest file for review.py """

from models.review import Review
import unittest

r = Review()


class TestReview(unittest.TestCase):
    """ unit tests for review """

    def test_review_place(self):
        self.assertTrue(isinstance(r.place_id, str))

    def test_review_user(self):
        self.assertTrue(isinstance(r.user_id, str))

    def test_review_text(self):
        self.assertTrue(isinstance(r.text, str))

if __name__ == '__main__':
    HBNBCommand().cmdloop()
