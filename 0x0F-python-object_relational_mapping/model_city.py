#!/usr/bin/python3
"""Python file similar to model_state.py named model_city.py 
   that contains the class definition of a City"""


from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """
    class that represents cities in MySQL database
    Inherits from Base class

    Attributes:
      id: auto-integrated, unqiue inter representing primary key of states.
      name: string with maximum length of 128 characters.
    """

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
