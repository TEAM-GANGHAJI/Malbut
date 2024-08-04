from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text, JSON
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime, timezone

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    username = Column(String(50), index=True)
    user_type = Column(String(10))
    # email = Column(String(50), unique=True, index=True)
    created_at = Column(DateTime, nullable=True, default=datetime.now(timezone.utc))
    
    