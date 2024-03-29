from jose import jwt
from datetime import datetime, timedelta
from typing import Union, Any
import os
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

ACCESS_TOKEN_EXPIRE_MINUTES = 30 #30 minutes
REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7
ALGORITHM = os.getenv("ALGORITHM")
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
JWT_REFRESH_SECRET_KEY = os.getenv("JWT_REFRESH_SECRET_KEY")


def create_access_token(subject:Union[str, Any], expires_delta:int= None)->str:
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        
    to_encode = {"exp":str(expires_delta), "sub": str(subject)}
    
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, algorithm=ALGORITHM)
    
    # encoded_jwt = ""
    
    return encoded_jwt

def create_refresh_token(subject: Union[str, Any], expires_delta: int= None) -> str:
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        
    to_encode = {"exp":str(expires_delta), "sub": str(subject)}
    
    encoded_jwt = jwt.encode(to_encode, JWT_REFRESH_SECRET_KEY, algorithm=ALGORITHM)
    
    # encoded_jwt = ""
    return encoded_jwt