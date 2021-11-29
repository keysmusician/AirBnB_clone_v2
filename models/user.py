#!/usr/bin/python3
"""`User` class definition."""
from models.base_model import BaseModel, Base
from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import String


class User(BaseModel, Base):
    """A HBnB user."""
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    places = relationship("Place", backref="user", cascade="all")
    reviews = relationship("Review", backref="user", cascade="all")
