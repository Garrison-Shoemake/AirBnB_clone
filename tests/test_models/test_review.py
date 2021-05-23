#!/usr/bin/python3
from models.review import Review
import unittest

r = Review()


class TestReview(unittest.TestCase):

    def test_review_place(self):
        self.assertTrue(type(r.place_id) is str)

    def test_review_user(self):
        self.assertTrue(type(r.user_id) is str)

    def test_review_text(self):
        self.assertTrue(type(r.text) is str)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
