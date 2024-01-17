from fastapi import APIRouter
from api.v1.todo import _create
# from database._base_class import Base
# from database._database import engine

# metadata = Base.metadata

# metadata.create_all(engine)

todo_router = APIRouter()

todo_router.include_router(_create.todo_create_route, prefix="", tags=["todos"])

