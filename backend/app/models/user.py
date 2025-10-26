from sqlalchemy import Column, Integer, String, Enum as SqlEnum
from app.database.db_setup import Base
from enum import Enum

class Role(Enum):
    guard = "guard"
    supervisor = "supervisor"
    manager = "manager"
    admin = "admin"
    
class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(120), unique=True, index=True)
    password_hash = Column(String(255), nullable=False)
    role = Column(SqlEnum(Role), default=Role.guard)
    
    def __repr__(self):
        return f"<User(name='{self.name}', role='{self.roll.value}')>"