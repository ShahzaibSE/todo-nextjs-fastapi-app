from fastapi import APIRouter

router = APIRouter(
    prefix="/todo",
    tags=["todo"],
    responses={404: {"description": "Not found"}},
)

@router.get("/test")
def test():
    return "Hello Test, it's a success"