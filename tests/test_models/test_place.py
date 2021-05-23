#!/usr/bin/python3
from models.place import Place
import unittest


p = Place()

class TestPlace(unittest.TestCase):

     def test_city_id(self):
        self.assertTrue(type(p.city_id) is str)

     def test_user_id(self):
        self.assertTrue(type(p.user_id) is str)

     def test_place_name(self):
        self.assertTrue(type(p.name) is str)

     def test_description(self):
        self.assertTrue(type(p.description) is str)

     def test_number_rooms(self):
        self.assertTrue(type(p.number_rooms) is int)

     def test_bathrooms(self):
        self.assertTrue(type(p.number_bathrooms) is int)

     def test_max_guest(self):
        self.assertTrue(type(p.max_guest) is int)

     def test_price_by_night(self):
        self.assertTrue(type(p.price_by_night) is int)

     def test_latitude(self):
        self.assertTrue(type(p.latitude) is float)

     def test_longitude(self):
        self.assertTrue(type(p.longitude) is float)

     def test_aminity_ids(self):
        self.assertTrue(type(p.amenity_ids) is list)

if __name__ == '__main__':
    unittest.main()
