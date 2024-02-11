#!/usr/bin/python3
import uuid
from uuid import uuid4
import datetime


# make a class called basemodel (done)
# then make an attribute called ID use the uuid.uuid4 (done)

class BaseModel:
    def __init__(self):
        self.format = 
        self.id = str(uuid4())
        self.created_at = datetime.datetime()
        self.updated_at = datetime.datetime()
    
    def __str__(self):
        clname = self.__str__.__name__
        return f"{clname} {self.id} {self.__dict__}"
    
    # make a fun save to save the the public attribute updated_at to the current date 
    def save(self):
        """update the public attribute updated_at to the current date. """
        self.updated_at = datetime.today()
        #dont forget to store it

   
