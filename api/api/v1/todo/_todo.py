from fastapi import APIRouter
from api.v1.todo import _create

todo_router = APIRouter()

todo_router.include_router(_create.todo_create_route, prefix="", tags=["todos"])

