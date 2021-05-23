#!/usr/bin/python3
""" place class inherits from BaseModel """


from models.base_model import BaseModel


class Place(BaseModel):
    """ place class has several class attributes """


    city_id = "" # will be City.id
    user_id = "" # will be User.id
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = [] #empty list, will be Amenity.id late
