from fastapi import APIRouter
from schemas._user import UserCreate

router = APIRouter(
    prefix="/user",
    tags=["/user"],
    responses={404: {"description": "Not found"}},
)

@router.post("/signup", response_model=UserCreate)
def signup(user_data):
    try:
        return {
            "status":True,
            "resCode": 200,
            "message": "Signed up successfully",
            "isError": False
        }
    except:
        return {
            "status": False,
            "resCode": 500,
            "message": "Internal error in the server",
            "isError": True
        }

