#!/usr/bin/python3
"""This is the city class"""

import sqlalchemy
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from models.base_model import BaseModel
from sqlalchemy.orm import relationship
from os import getenv


class City(BaseModel, Base):
    """
    This is the class for City
    """
    __tablename__ = 'cities'

    if getenv('HBNB_TYPE_STORAGE') == 'db':

        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        state = relationship("State")
        places = relationship("Place", cascade="all, delete-orphan")

    else:
        name = ""
        state_id = ""
