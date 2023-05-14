#!/usr/bin/python3
from models.base_model import BaseModel
""" The model for creating state object """


class State(BaseModel):

    name = ""

    def __str__(self):
        """ The str function """
        return f"[State] ({self.id}) {self.__dict__}"
