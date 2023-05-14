#!/usr/bin/python3
from models.base_model import BaseModel
""" The model for creating review object """


class Review(BaseModel):

    place_id = ""
    user_id = ""
    text = ""

    def __str__(self):
        """ The str function  """

        return f"[Review] ({self.id}) {self.__dict__}"
