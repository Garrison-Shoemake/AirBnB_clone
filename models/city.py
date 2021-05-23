#!/usr/bin/python3
""" City class, inherits from BaseModel """


from models.base_model import BaseModel


class City(BaseModel):

    """ city class has two attributes """

    state_id = ""  # this attribute will be the State.id
    name = ""
