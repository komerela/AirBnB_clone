#!/usr/bin/python3
"""
DBStorage schema using SQLAlchemy && MySQL
"""
import sqlalchemy
from sqlalchemy import create_engine
from os import getenv
from models.city import City
from models.place import Place
from models.base_model import BaseModel, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from models.amenity import Amenity
from models.review import Review
from models.state import State
from models.user import User
import models


class DBStorage:
    """
    database storage class
    """

    __engine = None
    __session = None

    def __init__(self):
        """
            Instantiation of a database storage class
        """
        user = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        database = getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.
            format(user, password, host, database), pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
            Queries database for specified classes
            Parameters:
                cls (object): the class to query
            Return:
                a dictionary of objects of the corresponding cls
        """
        to_query = []
        new_dict = {}
        if cls is not None:
            results = self.__session.query(eval(cls.__name__)).all()
            for row in results:
                key = row.__class__.__name__ + '.' + row.id
                new_dict[key] = row
        else:
            for key, value in models.classes.items():
                try:
                    self.__session.query(models.classes[key]).all()
                    to_query.append(models.classes[key])
                except BaseException:
                    continue
            for classes in to_query:
                results = self.__session.query(classes).all()
                for row in results:
                    key = row.__class__.__name__ + '.' + row.id
                    new_dict[key] = row
        return new_dict

    def new(self, obj):
        """
        add the object to the current database session (self.__session)
        """
        self.__session.add(obj)

    def save(self):
        """
        commit all changes of the current database session (self.__session)
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        delete from the current database session obj if not None
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
            Restarts the database engine session
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session

    def close(self):
        """
            Closes the session and destroys it
        """
        self.__session.remove()
