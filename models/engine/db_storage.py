#!/usr/bin/python3
"""This module defines a class to manage database for hbnb clone"""
from models.base_model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from os import getenv


classes = {'User': User, 'Place': Place,
           'State': State, 'City': City, 'Amenity': Amenity,
           'Review': Review}


class DBStorage:
    """Manages database storage engine mode"""
    __engine = None
    __session = None

    def __init__(self):
        """Initializes data"""
        usr = getenv('HBNB_MYSQL_USER')
        psw = getenv('HBNB_MYSQL_PWD')
        hst = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(usr,
                                                                           psw,
                                                                           hst,
                                                                           db),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session all objects depending
        of the class name"""
        session = self.__session
        d = {}
        if cls and cls in classes.values():
            ins = session.query(cls).all()
            for obj in ins:
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                value = obj
                d[key] = value
        elif cls is None:
            for cl in classes.values():
                ins = session.query(cl).all()
                for obj in ins:
                    key = "{}.{}".format(obj.__class__.__name__, obj.id)
                    value = obj
                    d[key] = value
        return d

    def new(self, obj):
        """add the object to the current database session"""
        if obj:
            self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        self.__session = scoped_session(session_factory)
