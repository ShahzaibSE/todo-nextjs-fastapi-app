from fastapi import APIRouter, Body
from schemas._user import UserCreate

router = APIRouter()

@router.post("/test")
def test(data):
    try:
        return {
            "status":True,
            "resCode": 200,
            "message": "Tested successfully",
            "isError": False,
        }
    except:
        return {
            "status": False,
            "resCode": 500,
            "message": "Internal error in the server",
            "isError": True
        }

