from fastapi import APIRouter, Body
from schemas._user import UserCreate

router = APIRouter(
    prefix="/user",
    tags=["/user"],
    responses={404: {"description": "Not found"}},
)

@router.post("/test")
def test(data):
    try:
        return {
            "status":True,
            "resCode": 200,
            "message": "Tested successfully",
            "isError": False,
            "data":req
        }
    except:
        return {
            "status": False,
            "resCode": 500,
            "message": "Internal error in the server",
            "isError": True
        }

