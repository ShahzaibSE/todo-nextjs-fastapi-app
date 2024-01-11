from database._database import get_db # starting database session
from sqlalchemy.orm import Session
from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException
from models._user import User

router = APIRouter()

# @router.post("/signup", response_model=User)
# def signup(user_data: User):
#     pass