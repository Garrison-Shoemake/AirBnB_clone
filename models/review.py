#!/usr/bin/python3
""" review class inherits from BaseModel """


from models.base_model import BaseModel


class Review(BaseModel):
    """ review has several public class attributes """

    place_id = "" # will be the Place.id
    user_id = "" # will be User.id
    text = ""
