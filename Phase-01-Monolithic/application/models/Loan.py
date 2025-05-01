from sqlalchemy import Column, Integer, String,  ForeignKey, DateTime, Enum
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from typing import Optional
from enum import Enum as PyEnum

Base=declarative_base()

class LoanStatus(PyEnum):
        active="ACTIVE"
        returned="RETURNED"

class Loan(Base):
    __tablename__='loans'
    id: int=Column(Integer, primary_key=True)
    user_id: int=Column(Integer, ForeignKey("users.id"), nullable=False)
    book_id: int=Column(Integer, ForeignKey("books.id"), nullable=False)
    issue_time: datetime=Column(Datetime, default=datetime.utcnow)
    original_due_time: datetime=Column(Datetime)
    status: str=Column(Enum(LoanStatus), nullable=False, default=LoanStatus.active)
    extension_count: Optional[int]=Column(Integer, default=0)
    extended_due_time: Optional[datetime]=Column(Datetime)