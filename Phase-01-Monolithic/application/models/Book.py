from sqlalchemy import Column, Integer, String, DateTime
from application.database.Base import Base
from datetime import datetime
from typing import Optional


class Book(Base):
    __tablename__='books'
    id: int=Column(Integer, primary_key=True)
    title: str=Column(String, unique=True, nullable=False)
    author: str=Column(String, nullable=False)
    isbn: str=Column(String, unique=True, nullable=False)
    copies: int=Column(Integer, nullable=False)
    available_copies: Optional[int]=Column(Integer)
    creation_time: datetime=Column(DateTime, default=datetime.utcnow)
    update_time: Optional[datetime]=Column(DateTime, onupdate=datetime.utcnow)