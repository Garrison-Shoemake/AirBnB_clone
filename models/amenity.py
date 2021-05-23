#!/usr/bin/python3
""" Amenity class, only oe attr """


from models.base_model import BaseModel


class Amenity(BaseModel):
    """ amenity only has one attr: its name """

    name = ""
