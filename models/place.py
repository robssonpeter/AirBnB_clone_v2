#!/usr/bin/python3
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship

""" The model for creating place object """


class Place(BaseModel, Base):
    """ represents place model in db

    attributes:
        __tablename__(str): name of the table
        city_id(sqlalchemy String): id of the city
        name(sqlalchemy String): name of the place
        description(sqlalchemy String): Description of the place
        number_rooms(sqlalchemy Integer): number of rooms
        number_bathrooms(sqlalchemy Integer): num of bathrooms
        max_guest(sqlalchemy Integer): Maximum guests
        price_by_night(sqlalchemy Integer): price per night
        latitude(sqlalchemy Float): Latitude coordinate
        longitude(sqlalchemy Float): Longitude coordinate
        reviews (sqlalchemy relationship): The Place to Review relationship.
        amenities (sqlalchemy relationship): The Place to Amenity relationship.
        amenity_ids (list): An id list of all amenities.
    """
    __tablename__ = "places"

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms =  Column(Integer, nullable=False, default=0)
    max_guest =  Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=False, default=0)
    longitude = Column(Float, nullable=False, default=0)
    amenities = relationship("Amenity", secondary="place_amenity",
                             viewonly=False)
    reviews = relationship("Review", backref="place", cascade="delete")
    amenity_ids = []
    

    def __str__(self):
        """ The str function  """

        return f"[Place] ({self.id}) {self.__dict__}"
