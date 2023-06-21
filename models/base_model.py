#!/usr/bin/python3
import uuid
from datetime import datetime
from models import storage
from sqlalchemy.orm import declarative_base
from sqlalchemy import String, Integer, Column, DateTime
""" The base model object definition """

Base = declarative_base()
class BaseModel:
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __str__(self):
        return f"[BaseModel] ({self.id}) {self.__dict__}"

    def save(self):
        """ The save function to store instances of objects """

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ adds objects to the dictionary """

        self.__dict__["__class__"] = "BaseModel"
        self.__dict__["created_at"] = self.created_at.isoformat()
        self.__dict__["updated_at"] = self.updated_at.isoformat()
        return self.__dict__

    def __init__(self, *args, **kwargs):
        """ The constructors function """

        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.id = self.id

        if len(kwargs.values()):
            for key in kwargs.keys():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        form = "%Y-%m-%dT%H:%M:%S.%f"
                        timed = datetime.strptime(kwargs[key], form)
                        self.__setattr__(key, timed)
                    else:
                        self.__setattr__(key, kwargs[key])
        storage.new(self)
