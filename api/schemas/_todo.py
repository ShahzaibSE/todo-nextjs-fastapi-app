# Pydantic schemas for data verification
from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class ToDoBase(BaseModel):
    text: str
    completed: Optional[bool] = False


class ToDoCreate(ToDoBase):
    pass
    
    
class ToDoCreate(ToDoCreate):
    pass

class ToDo(ToDoBase):
    id: int
    created_at: datetime
    updated_at: datetime
    