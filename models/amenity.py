#!/usr/bin/python3
"""`Amenity` class definition."""
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import String
from models.base_model import BaseModel, Base
from sqlalchemy import Column


class Amenity(BaseModel, Base):
    """An amenity available at an HBnB destination."""

    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary="place_amenity",
                                   backref="amenities")
