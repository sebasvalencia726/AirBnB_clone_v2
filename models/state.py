#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, ForeignKey, Column
from sqlalchemy.orm import relationship
import os

class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', backref='state',
                              cascade='all, delete-orphan')

    if os.getenv('HBNB_TYPE_STORAGE') == 'file':
        @property
        def cities(self):
            objects = {}
            for key, value in models.storage.all(models.City).items():
                if value.state_id == self.id:
                    objects[key] = value
            return objects
