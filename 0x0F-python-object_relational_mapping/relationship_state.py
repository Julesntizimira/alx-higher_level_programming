#!/usr/bin/python3
''' defines State and an instance Base = declarative_base()
'''
from sqlalchemy.orm import relationship, Mapped
from sqlalchemy import Column, Integer, String
from typing import List
from relationship_city import City, Base


class State(Base):
    '''represent states'''
    __tablename__ = "states"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String(128), nullable=False)
    cities: Mapped[List["City"]] = relationship(
            back_populates="state",
            cascade="all, delete-orphan"
            )
