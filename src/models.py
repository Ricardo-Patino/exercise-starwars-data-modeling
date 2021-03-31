import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Planet(Base):
    __tablename__ = 'planet'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    population = Column(String(40), nullable=False)
    gravity = Column(String(40))
    climate = Column(String(50))
    terrain = Column(String(50))
    created = Column(String(50))
    surface_water = Column(Integer)
    diameter = Column(Integer)
    orbital_period = Column(Integer)
    rotation_period = Column(Integer)
    pic = Column(String(50))
    url = Column(String(50))


    def to_dict(self):
        return {}

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(25), nullable=False)
    birth_year = Column(Date, nullable=False)
    created = Column(String(50))
    homeworld = Column(String(50))
    eye_color = Column(String(50))
    gender = Column(String(25))
    hair_color = Column(String(25))
    height = Column(Integer)
    mass = Column(Integer)
    skin_color = Column(String(20))
    pic = Column(String(50))
    url = Column(String(50))

    def to_dict(self):
        return {}

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(40), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False) 

    def to_dict(self):
        return {}     

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    usser_id = Column(Integer, ForeignKey(User.id))
    planet_id = Column(String(40),ForeignKey(Planet.id))
    person_id = Column(String(25),ForeignKey(Person.id))

    def to_dict(self):
        return {}

render_er(Base, 'diagram.png')


# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

#     def to_dict(self):
#         return {}

# ## Draw from SQLAlchemy base
# render_er(Base, 'diagram.png')