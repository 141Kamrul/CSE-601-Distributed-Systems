from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from typing import Optional
from application.database.Base import Base

class Loan(Base):
    __tablename__='loans'
    id: int=Column(Integer, primary_key=True)
    user_id: int=Column(Integer, ForeignKey("users.id"), nullable=False)
    book_id: int=Column(Integer, ForeignKey("books.id"), nullable=False)
    issue_time: datetime=Column(DateTime, default=datetime.utcnow)
    original_due_time: datetime=Column(DateTime)
    return_time: datetime=Column(DateTime, default=None)
    status: str=Column(String(10), default="ACTIVE")
    extension_count: Optional[int]=Column(Integer, default=0)
    extended_due_time: Optional[datetime]=Column(DateTime)