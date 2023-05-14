import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """The base model class that will be inherited by all other models"""

    id = str(uuid.uuid4())
    created_at = datetime.now()
    updated_at = datetime.now()

    def __str__(self):
        return f"[BaseModel] ({self.id}) {self.__dict__}"

    def __class__(self):
        return "BaseModel"

    def to_dict(self):
        self.__dict__["__class__"] = "BaseModel"
        self.__dict__["created_at"] = str(self.created_at.isoformat())
        self.__dict__["updated_at"] = str(self.updated_at.isoformat())
        return self.__dict__

    def save(self):
        self.updated_at = datetime.now()
        storage.save()

    def __init__(self, *args, **kwargs):
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.id = self.id

        if len(kwargs.values()):
            for key in kwargs.keys():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        timed = datetime.strptime(kwargs[key], "%Y-%m-%dT%H:%M:%S.%f")
                        self.__setattr__(key, timed)
                    else:
                        self.__setattr__(key, kwargs[key])
        storage.new(self)
