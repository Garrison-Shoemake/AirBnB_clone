#!/usr/bin/python3
""" Doc String """


from models.base_model import BaseModel


class User(BaseModel):

    """ Inherits from BaseModel with varying public class attributes """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
