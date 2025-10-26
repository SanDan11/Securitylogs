from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class IncidentBase(BaseModel):
    title: str = Field(..., min_length=3, max_length=255)
    description: Optional[str] = Field(None, max_length=255)
    severity: str = Field(..., min_length=3, max_length=50)
    location: str = Field(..., min_length=2, max_length=100)
    
class IncidentCreate(IncidentBase):
    guard_id: int
    
class IncidentOut(IncidentBase):
    id: int
    date_reported: datetime
    guard_id: int
    
    class Config:
        from_attributes = True