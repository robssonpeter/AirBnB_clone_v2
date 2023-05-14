#!/usr/bin/python3
from models.base_model import BaseModel
""" The model for creating city object """


class City(BaseModel):

    state_id = ""
    name = ""

    def __str__(self):
        """ The str function """

        return f"[City] ({self.id}) {self.__dict__}"
