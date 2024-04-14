#!/usr/bin/python3
"""python file that contains the class definition
of a State and an instance Base = declarative_base()"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    State class that represents state in MySQL database
    Inherits from Base class

    Attributes:
      id: auto-integrated, unqiue inter representing primary key of states.
      name: string with maximum length of 128 characters.
    """

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
