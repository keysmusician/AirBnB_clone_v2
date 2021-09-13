#!/usr/bin/python3
"""`State` class definition."""
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """A U.S. state."""
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all", backref="state")

    @property
    def cities(self):
        """Return the list of cities matching this state."""
        return [city for city in storage.all(City).values()
                if city.state_id == self.id]

if __name__ == '__main__':
    # Storage is defined prior to importing these modules, but needs to be
    # imported here if running stand-alone.
    from models import storage
