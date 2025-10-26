from pydantic import BaseModel, EmailStr, Field
from enum import Enum

class Role(str, Enum):
    guard = "guard"
    supervisor = "supervisor"
    manager = "manager"
    admin = "admin"

class UserBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    email: EmailStr
    role: Role = Role.guard
    
class UserCreate(UserBase):
    password: str = Field(..., min_length=6, max_length=128)
    
class UserOut(UserBase):
    id: int

    class Config:
        from_attributes = True