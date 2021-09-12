#!/usr/bin/python3
"""
Defines `BaseModel`, a base class for all models, and `Base`, the declarative
base class from SQLAlchemy.

"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime

Base = declarative_base()


class BaseModel:
    """A base class for all HBnB models."""
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow(), nullable=False)

    def __init__(self, *args, **kwargs):
        """Instantiate a new model."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        # Set each keyword argument as an instance attribute
        for k, v in kwargs.items():
            # Do not set `__class__`, since it is set automatically
            if k == '__class__':
                continue

            # Convert datetime strings to datetime objects
            if k in ('updated_at', 'created_at'):
                v = datetime.strptime(v, '%Y-%m-%dT%H:%M:%S.%f')

            setattr(self, k, v)

    def __str__(self):
        """Return a string representation of the instance."""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.to_dict())

    def save(self):
        """Update `updated_at` with current time when instance is modified."""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dictionary format."""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        if hasattr(self, '_sa_instance_state'):
            del dictionary['_sa_instance_state']
        return dictionary

    def delete(self):
        """Delete the current instance from storage."""
        from models import storage
        storage.delete(self)
