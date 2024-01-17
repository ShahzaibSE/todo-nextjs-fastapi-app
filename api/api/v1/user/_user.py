from fastapi import APIRouter
from api.v1.user import _create
# from database._base_class import Base
# from database._database import engine

# metadata = Base.metadata

# metadata.create_all(engine)

user_router: APIRouter = APIRouter()

user_router.include_router(_create.create_route, prefix="", tags=["user"])