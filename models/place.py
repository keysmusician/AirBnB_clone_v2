#!/usr/bin/python3
"""`Place` class definition."""
from models import storage
from models.base_model import BaseModel, Base
from sqlalchemy import Column
from sqlalchemy.sql.schema import ForeignKey, Table
from sqlalchemy.sql.sqltypes import Float, Integer, String
from sqlalchemy.orm import relationship


# Association table for Place-Amentity many-to-many relationship
place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id", String(60), ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column("amenity_id", String(60),
                             ForeignKey("amenities.id"), primary_key=True,
                             nullable=False)
                      )


class Place(BaseModel, Base):
    """A place to stay."""
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    reviews = relationship("Review", backref="place", cascade="all")
    amenities = relationship("Amenity", secondary=place_amenity,
                             viewonly=False)
    amenity_ids = []

    @property
    def reviews(self):
        """
        Return the list of `Review` instances with `place_id` == `self.id`.

        """
        from models.review import Review
        return [review for review in storage.all(Review).values()
                if review.place_id == self.id]

    @property
    def amenities(self):
        """Return the list of `Amenity` instances linked to this place."""
        from models.amenity import Amenity
        return [amenity for amenity in storage.all(Amenity).values
                if amenity.id in self.amenity_ids]

    @amenities.setter
    def amenities(self, amenity):
        """Validate and handle additions to amenities at this place."""
        from models.amenity import Amenity
        if type(amenity) is Amenity:
            self.amenity_ids.append(amenity.id)
