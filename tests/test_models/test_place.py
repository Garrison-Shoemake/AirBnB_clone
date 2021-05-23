#!/usr/bin/python3
""" tests for teestplace """
from models.place import Place
import unittest


p = Place()


class TestPlace(unittest.TestCase):

    """ tests for testplace """

    def test_city_id(self):
        self.assertTrue(isinstance(p.city_id, str))

    def test_user_id(self):
        self.assertTrue(isinstance(p.user_id, str))

    def test_place_name(self):
        self.assertTrue(isinstance(p.name, str))

    def test_description(self):
        self.assertTrue(isinstance(p.description, str))

    def test_number_rooms(self):
        self.assertTrue(isinstance(p.number_rooms, int))

    def test_bathrooms(self):
        self.assertTrue(isinstance(p.number_bathrooms, int))

    def test_max_guest(self):
        self.assertTrue(isinstance(p.max_guest, int))

    def test_price_by_night(self):
        self.assertTrue(isinstance(p.price_by_night, int))

    def test_latitude(self):
        self.assertTrue(isinstance(p.latitude, float))

    def test_longitude(self):
        self.assertTrue(isinstance(p.longitude, float))

    def test_aminity_ids(self):
        self.assertTrue(isinstance(p.amenity_ids, list))

if __name__ == '__main__':
    unittest.main()
