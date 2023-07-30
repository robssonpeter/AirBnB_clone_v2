#!/usr/bin/python3
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import String, Column
""" The model for creating state object """


class State(BaseModel, Base):
    __tablename__ = "states"

    name = Column(String(128), nullable=False)

    def __str__(self):
        """ The str function """
        return f"[State] ({self.id}) {self.__dict__}"
