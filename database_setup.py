import sys

from sqlalchemy import create_engine
# Creates a new Engine instance
from sqlalchemy.ext.declarative import declarative_base
# Imports the Base class from SA 
from sqlalchemy.orm import relationship
# Imports the MetaData container object which houses
# variables required in creating tables
from sqlalchemy import Column, ForeignKey, Integer, String, Table

Base = declarative_base()

class Shelter(Base):
    __tablename__ = 'shelter'
    
    name = Column(String(45), nullable=False)
    address = Column(String(85), nullable=False)
    city = Column(String(45), nullable=False)
    state = Column(String(45), nullable=False)
    email = Column(String(45))
    website = Column(String(45))
    zipCode = Column(String(45))
    id = Column(Integer, primary_key=True)

class Puppy(Base):
    __tablename__ = 'puppy'
    name = Column(String(45))
    dateOfBirth = Column(Integer)
    breed = Column(String(45))
    gender = Column(String(25), nullable=False)
    weight = Column(Integer)
    picture = Column(String)
    shelter_id = Column(Integer, ForeignKey('shelter.id'))
    shelter = relationship(Shelter)
    id = Column(Integer, primary_key=True)
    


engine = create_engine('sqlite:///puppyshelter.db')

Base.metadata.create_all(engine)