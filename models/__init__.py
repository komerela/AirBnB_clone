#!/usr/bin/python3
"""create a unique FileStorage instance for your application"""

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from os import getenv
from models.engine.db_storage import DBStorage

classes = {"User": User, "BaseModel": BaseModel,
           "Place": Place, "State": State,
           "City": City, "Amenity": Amenity,
           "Review": Review}

if getenv('HBNB_TYPE_STORAGE') == 'db':
    storage = DBStorage()

else:
    storage = FileStorage()

storage.reload()
