from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database.db_setup import Base

class Incident(Base):
    __tablename__ = "incidents"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(String(255), nullable=True)
    severity = Column(String(50), nullable=False)
    location = Column(String(100), nullable=False)
    date_reported = Column(DateTime, default=datetime.utcnow)
    
    guard_id = Column(Integer, ForeignKey("users.id"))
    guard = relationship("User")
    
    def __repr__(self):
        return f"<Incident(severity=`{self.severity}`, location=`{self.location}`)>"