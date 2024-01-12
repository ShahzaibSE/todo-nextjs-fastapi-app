from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from database._base_class import Base
from datetime import datetime

class TODO(Base):
    __tablename__ = 'todos'
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, index=True)
    is_completed = Column(Boolean, default=False)
    # created_at = Column(DateTime, server_default=func.now())
    # updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    # owner_id = Column(Integer, ForeignKey("users.id"))
    # owner = relationship("User", back_populates="todos")
    
    def __str__(self):
        return f"Todo #{self.id}: {self.text}, Completed: {self.is_completed}"