from database._database import get_db # starting database session
from sqlalchemy.orm import Session
from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException
from schemas._user import User as UserResponse, UserCreate
from models._user import User
from lib._crypt import get_password, verify_password
from fastapi.responses import ORJSONResponse


create_route = APIRouter()

@create_route.post("/signup/", response_model=UserResponse)
def signup(user_data: UserCreate, user_db: Session = Depends(get_db)):
    """add new user"""
    try:
        # password = get_password(user_data.password)
        # print("Hashed password")
        # print(password)
        password = ""
        newUser = User(
            lname=user_data.lname,
            fname=user_data.f_name,
            email=user_data.email,
            password=password,
            created_at=datetime.utcnow()
        )
        print("New User")
        print(newUser)
        user_db.add(newUser)
        user_db.commit()
        user_db.refresh(newUser)
        user_db.close()
       
    except:
        HTTPException(status_code=500, detail="Couldn't register due to an error")