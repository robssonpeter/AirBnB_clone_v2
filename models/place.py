#!/usr/bin/python3
from models.base_model import BaseModel
""" The model for creating place object """


class State(BaseModel):

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __str__(self):
        """ The str function  """

        return f"[Place] ({self.id}) {self.__dict__}"
