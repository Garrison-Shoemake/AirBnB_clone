#!/usr/bin/python3
""" State class, inherits from BaseModel """

from models.base_model import BaseModel

class State(BaseModel):
    """ State only has one attribute, its name """

    name = ""
