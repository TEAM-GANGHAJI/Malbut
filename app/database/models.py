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
    phone = Column(String(50), unique=True, index=True)
    created_at = Column(DateTime, nullable=True, default=datetime.now(timezone.utc))
    
# class Correction(Base):
#     __tablename__ = "corrections"

#     id = Column(Integer, primary_key=True, index=True)
#     user_id = Column(Integer, ForeignKey("users.id"))
#     original_text = Column(Text)
#     corrected_text = Column(Text)
#     overall_score = Column(Integer)
#     correctness_alerts = Column(Integer)
#     coherence_score = Column(Integer)
#     clarity = Column(String)
#     explanation = Column(Text)
#     grammar_rule = Column(Text)
#     created_at = Column(DateTime(timezone=True), server_default=func.now())

#     user = relationship("User", back_populates="corrections")