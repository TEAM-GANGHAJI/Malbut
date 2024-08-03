from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import List, Optional

class UserBase(BaseModel):
    username: str
    # email: EmailStr
    user_type: str

class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    username: Optional[str] = None
    # email: Optional[EmailStr] = None
    user_type: Optional[str] = None

class UserDelete(BaseModel):
    id: int

class User(UserBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
