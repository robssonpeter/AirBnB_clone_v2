#!/usr/bin/python3
""" Defining the Class for User """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String


class User(BaseModel, Base):
    """ The user model for the database

    Attributes:
        __tablename__(str): Table in db
        email(sqlalchemy String): the email column
        password(sqlalchemy String): password for user
        first_name(sqlalchemy String)
    """
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship("Place", backref="user", cascade="delete")

    def __str__(self):
        """ The str function """

        return f"[User] ({self.id}) {self.__dict__}"

    def __init__(self, *args, **kwargs):
        """ The class constructor for User """

        super().__init__(*args, **kwargs)
