from fastapi import APIRouter
from api.v1.user import _create

user_router: APIRouter = APIRouter()

user_router.include_router(_create.create_route, prefix="", tags=["user"])