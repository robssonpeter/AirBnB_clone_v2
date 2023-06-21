""" Database storage class """
from sqlalchemy import create_engine
from sqlalchemy.orm import create_session, declarative_base
import os
from os import getenv
from json import JSONEncoder
from file_storage import ObjectEncoder
from city import City
from state import State
from place import Place
from review import Review
from user import User
from amenity import Amenity

Base =  declarative_base()

class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        username = os.environ.get('HBNB_MYSQL_USER')
        password = os.environ.get('HBNB_MYSQL_PWD')
        host = os.environ.get('HBNB_MYSQL_HOST')
        db = os.environ.get('HBNB_MYSQL_DB')
        statement = f"""
            mysql://{username}:{password}
            @{host}:3306/{db}
        """
        self.__engine = create_engine(statement, pool_pre_ping=True)
        self.__session = create_session(bind=self.__engine)
        self.__engine.dialect = "mysql"
        self.__engine.driver = "mysqldb"
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        if cls == None:
            data = self.__session.query(State).all()
            data.extend(self.__session.query(City))
            data.extend(self.__session.query(Place))
            data.extend(self.__session.query(Review))
            data.extend(self.__session.query(User))
            data.extend(self.__session.query(Amenity))
            return ObjectEncoder().encode(self.__session.query().all())
        else:
            return ObjectEncoder().encode(self.__session.query(cls).filter(name=cls.name))

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, cls=None):
        if cls is not None:
            self.__session.query(cls).filter(id = cls.id).delete()
            self.__session.commit()

    def reload(self):
        
