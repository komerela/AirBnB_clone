#!/usr/bin/python3
"""This is the base model class for AirBnB"""
import uuid
from datetime import datetime
import models
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey

Base = declarative_base()


class BaseModel:

    """
    Class defines common attributes/methods for other classes
    """

    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False,
                        default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False,
                        default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        if (len(kwargs) == 0):
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

        else:
            try:
                kwargs["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                kwargs["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")

            except KeyError:
                self.id = str(uuid.uuid4())
                self.created_at = datetime.now()
                self.updated_at = datetime.now()

            for key, val in kwargs.items():
                if "__class__" not in key:
                    setattr(self, key, val)

    def __str__(self):
        """returns a string repre for Base class
        """
        return ("[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__))

    def __repr__(self):
        """
        return a string representaion
        """
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                self.id, self.__dict__))

    def save(self):
        """
        updates the public instance attribute updated_at to new
        """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """
        creates dictionary of the class  and
            returns a dictionary of all the key values in __dict__
        """
        my_dict = dict(self.__dict__)
        if '_sa_instance_state' in my_dict:
            del my_dict['_sa_instance_state']
        my_dict["__class__"] = self.__class__.name__
        my_dict["created_at"] = self.created_at.strftime(
                "%Y-%m-%dT%H:%M:%S.%f")
        my_dict["updated_at"] = self.updated_at.strftime(
                "%Y-%m-%dT%H:%M:%S.%f")
        return my_dict

    def delete(self):
        """
            delete current instance from storage(models.storage)
        """
        models.storage.delete(self)
