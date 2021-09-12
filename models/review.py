#!/usr/bin/python3
"""`Review` class definition."""
from sqlalchemy.sql.expression import null
from sqlalchemy.sql.schema import ForeignKey
from models.base_model import BaseModel, Base
from sqlalchemy import Column
from sqlalchemy.types import Integer, String


class Review(BaseModel, Base):
    """User reviews of an HBnB location."""
    __tablename__ = "reviews"
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
