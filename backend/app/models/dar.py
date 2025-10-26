from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.database.db_setup import Base
from datetime import date

class DailyActivityReport(Base):
    __tablename__ = "daily_activity_reports"
    
    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, default=date.today)
    shift = Column(String(50), nullable=False)
    summary = Column(String(255), nullable=True)
    
    guard_id = Column(Integer, ForeignKey("users.id"))
    guard = relationship("User")
    
    def __repr__(self):
        return f"<DAR(shift=`{self.shift}`, gaurd=`{self.guard_id}`)>"