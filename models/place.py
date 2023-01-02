#!/usr/bin/python3
"""Contains info about the Place class
"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, Table, Integer, Float, String, ForeignKey
import models
from os import getenv
from sqlalchemy.orm import relationship


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'), primary_key=True,
                             nullable=False))


class Place(BaseModel, Base):
    """This class inherits from the BaseModel class
    """
    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if getenv('HBNB_STORAGE_TYPE') == 'db':
        amenities = relationship('Amenity', secondary='place_amenity',
                                 backref='place_amenities',
                                 viewonly=False)
        reviews = relationship('Review', backref='place',
                               cascade='all, delete')
    else:
        @property
        def reviews(self):
            rev_list = []
            for rev in models.storage.all(Review).values():
                if rev.place_id == self.id:
                    rev_list.append(rev)
            return rev_list

        @property
        def amenities(self):
            list_a = []
            for key, val in models.storage.all(Amenity).items():
                if key in self.amenity_ids:
                    list_a.append(val)
            return list_a

        @amenities.setter
        def amenities(self, obj=None):
            if type(obj) is Amenity and obj.id not in self.amenity_ids:
                new_amenity_id = 'Amenity' + '.' + obj.id
                amenity_ids.append(new_amenity_id)
