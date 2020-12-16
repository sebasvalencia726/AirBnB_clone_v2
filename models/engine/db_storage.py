#!/usr/bin/python3
"""New engine DBStorage"""
import os
from models.base_model import BaseModel, Base
from models.review import Review
from models.user import User
from models.city import City
from models.place import Place
from models.state import State
from models.amenity import Amenity
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


class DBStorage:
    """Storage with SQL, the engine must be linked to the
    MySQL database and user, all of the following values must be
    retrieved via environment variables:

    MySQL user: HBNB_MYSQL_USER
    MySQL password: HBNB_MYSQL_PWD
    MySQL host: HBNB_MYSQL_HOST (here = localhost)
    MySQL database: HBNB_MYSQL_DB

    Private class attributes:
        __engine: set to None
        __session: set to None
    """
    __engine = None
    __session = None

    def __init__(self):
        """Create an instance of DBStorage"""
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                os.getenv('HBNB_MYSQL_USER'),
                os.getenv('HBNB_MYSQL_PWD'),
                os.getenv('HBNB_MYSQL_HOST'),
                os.getenv('HBNB_MYSQL_DB')), pool_pre_ping=True
        )
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """returns a dictionary
        Args:
            cls: class name
        """
        if cls:
            return self.__session.query(cls).all()
        return self.__session.query(User,
                                    Amenity,
                                    Place,
                                    State,
                                    City,
                                    Review).all()

    def new(self, obj):
        """Adds the object to the current database session
        Args:
            obj: object to be added.
        """
        if obj:
            self.__session.add(obj)

    def save(self):
        """Commits all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None
        Args:
            obj: object
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database
        Alse creates the current database session (self.__session) from the
        engine (self.__engine) by using a sessionmaker - the option
        expire_on_commit is set to False; and scoped_session -
        to make sure your Session is thread-safe.
        """
        Base.metadata.create_all(self.__engine)
        sess = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(sess)
