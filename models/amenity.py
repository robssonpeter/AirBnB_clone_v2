#!/usr/bin/python3
from models.base_model import BaseModel
""" The model for creating amenity object """


class Amenity(BaseModel):

    name = ""

    def __str__(self):
        """ The str function  """

        return f"[Amenity] ({self.id}) {self.__dict__}"
