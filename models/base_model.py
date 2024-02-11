#!/usr/bin/python3
import uuid
import datetime
from uuid import uuid4


class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def save(self):
        """Update the public attribute updated_at to the current date."""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict

    def __str__(self):
        clname = self.__class__.__name__
        return f"{clname} {self.id} {self.__dict__}"
