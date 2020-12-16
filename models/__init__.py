#!/usr/bin/python3
"""This module instantiates an object of class FileStorage
Depending of the value of the environment variable HBNB_TYPE_STORAGE:
    If equal to db:
        Import DBStorage class in this file
        Create an instance of DBStorage and store it in the
        variable storage.
    Else:
        Import FileStorage class in this file
        Create an instance of FileStorage and store it in the variable storage
"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from models.place import Place
from models.user import User
from models.review import Review
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.state import State
import os

if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()
