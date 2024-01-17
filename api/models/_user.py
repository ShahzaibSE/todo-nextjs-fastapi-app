from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, func
from sqlalchemy.orm import sessionmaker, relationship
from database._base_class import Base
from datetime import datetime

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True, autoincrement="auto")
    lname = Column(String)
    fname = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String, unique=True)
    created_at = Column(DateTime, server_default=func.now())
    todos = relationship("TODO", backref="owner_todos", cascade="all, delete-orphan")

    