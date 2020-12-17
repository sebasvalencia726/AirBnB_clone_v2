#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table
from os import getenv
from sqlalchemy.orm import relationship
import models

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship("Review",
                               backref="place",
                               cascade="all, delete, delete-orphan")
        amenities = relationship("Amenity",
                                 secondary=place_amenity,
                                 viewonly=False)
    else:
        @property
        def reviews(self):
            """returns the list of City instances with state_id equals
            to the current State.id"""
            obj = models.storage.all(Review)
            ls = []
            for review in obj.values():
                if review.state_id == self.id:
                    ls.append(review)
            return ls

        @property
        def amenities(self):
            """returns the list of City instances with state_id equals
            to the current State.id"""
            obj = models.storage.all(Amenity)
            ls = []
            for amenity in obj.values():
                if amenity.place_id == self.id:
                    ls.append(amenity)
            return ls

        @amenities.setter
        def amenities(self, obj=None):
            """handles append method for adding an Amenity.id to the attribute
            amenity_ids"""
            if obj and obj.__class__.__name__ == "Amenity":
                self.amenity_ids.append(obj.id)
