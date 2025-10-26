import datetime

from pydantic import BaseModel, Field
from typing import Optional

class DARBase(BaseModel):
    date: datetime.date = Field(default_factory=datetime.date.today)
    shift: str = Field(..., min_length=1, max_length=50)
    summary: str = Field(..., min_length=3, max_length=255)
    
class DARCreate(DARBase):
    guard_id: int
    
class DAROut(DARBase):
    id: int
    guard_id: int
    
    class Config:
        from_attributes = True