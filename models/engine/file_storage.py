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
        return self.__objects

    def new(self, obj):
        obtype = type(obj).__name__
        type_list = obtype.split(".")
        self.__objects[type_list[0]+"."+obj.id] = obj

    def save(self):
        with open(self.__file_path, "w", encoding="UTF-8") as file:
            """string = json.dumps(self.__objects)"""
            string = ObjectEncoder().encode(self.__objects)
            file.write(string)
    
    def delete(self, obj=None):
        if obj is not None:
            del self.__objects[f"{type(obj).__name__}.{obj.id}"]


    def reload(self):
        if isfile(self.__file_path):
            with open(self.__file_path, "r", encoding="UTF-8") as file:
                string = file.read()

                if len(string):
                    self.__objects = json.loads(string)
