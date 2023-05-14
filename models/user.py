#!/usr/bin/python3
""" Defining the Class for User """
from models.base_model import BaseModel


class User(BaseModel):
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __str__(self):
        """ The str function """

        return f"[User] ({self.id}) {self.__dict__}"

    def __init__(self, *args, **kwargs):
        """ The class constructor for User """

        super().__init__(*args, **kwargs)
