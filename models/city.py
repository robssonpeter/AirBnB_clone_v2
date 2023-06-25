#!/usr/bin/python3
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
""" The model for creating city object """


class City(BaseModel, Base):

    __tablename__ = 'cities'
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    name = Column(String(128), nullable=False)
    places = relationship('Place', backref='city', cascade="delete")

    def __str__(self):
        """ The str function """

        return f"[City] ({self.id}) {self.__dict__}"
