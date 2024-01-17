from schemas._todo import Todo as TodoResponse
from models._todo import TODO
from database._database import get_db # starting database session
from sqlalchemy.orm import Session
from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException, Body
from schemas._todo import TodoCreate
# from database._base_class import Base
# from database._database import engine

# metadata = Base.metadata

# metadata.create_all(engine)

# Creating router.
todo_create_route = APIRouter()

@todo_create_route.post("/create/", response_model=TodoResponse)
def createToDo(todo: TodoCreate, db: Session = Depends(get_db)):
    # try:
    """
    Create a new todo.
    """
    db_todo = TODO(
        text=todo.text,
        is_completed=todo.is_completed,
    )

    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo
    # except:
    #     HTTPException(status_code=500, detail="Couldn't register due to an error", headers={'Content-Type': 'application/json'})

