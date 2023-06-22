#!/usr/bin/python3
import json
from os.path import isfile
from json import JSONEncoder
from datetime import datetime


class ObjectEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()
        return o.__dict__


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        if cls is None:
            return self.__objects
        filtered_objects = {}
        for key, value in self.__objects.items():
            if cls == value.__class__:
                filtered_objects[key] = value
        return filtered_objects

    def new(self, obj):
        obtype = type(obj).__name__
        type_list = obtype.split(".")
        self.__objects[type_list[0]+"."+obj.id] = obj

    def save(self):
        with open(self.__file_path, "w", encoding="UTF-8") as file:
            string = ObjectEncoder().encode(self.__objects)
            file.write(string)

    def reload(self):
        if isfile(self.__file_path):
            with open(self.__file_path, "r", encoding="UTF-8") as file:
                string = file.read()

                if len(string):
                    self.__objects = json.loads(string)

    def delete(self, obj=None):
        if obj is None:
            return
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        if key in self.__objects:
            del self.__objects[key]


