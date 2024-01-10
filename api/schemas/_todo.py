# Pydantic schemas for data verification
from pydantic import BaseModel


class ToDoCreate(BaseModel):
    text: str
    completed: bool
    
class ToDoCreate(ToDoCreate):
    id: int