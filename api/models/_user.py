from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from api.database._database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    lname = Column(String)
    fname = Column(String)
    email = Column(String, unique=True, index=True)
    todos = relationship("TODOS", backref="owner", cascade="all, delete-orphan")

    