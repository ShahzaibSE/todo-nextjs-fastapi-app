# Pydantic schemas for data verification
from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class TodoBase(BaseModel):
    text: str
    is_completed: Optional[bool] = False


class TodoCreate(TodoBase):
    pass


class TodoUpdate(TodoBase):
    pass


class Todo(TodoBase):
    id: int
    created_at: datetime
    updated_at: datetime

    # class Config:
    #     from_attributes = True
    