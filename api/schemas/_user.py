# Pydantic schemas for data verification
from pydantic import BaseModel
from pydantic import EmailStr
from datetime import datetime

class UserBase(BaseModel):
   email: EmailStr
   
class UserCreate(UserBase):
   lname: str
   fname: str
   password: str
   
class User(UserCreate):
   # created_at: datetime
   pass