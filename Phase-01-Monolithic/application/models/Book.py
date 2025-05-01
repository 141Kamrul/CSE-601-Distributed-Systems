from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from typing import Optional

Base=declarative_base()

class Book(Base):
    __tablename__='books'
    id: int=Column(Integer, primary_key=True)
    title: str=Column(String, unique=True, nullable=False)
    author: str=Column(String, nullable=False)
    isbn: str=Column(String, unique=True, nullable=False)
    copies: int=Column(Integer, nullable=False)
    available_copies: int=Column(Integer,nullable=False)
    creation_time: datetime=Column(datetime, default=datetime.utcnow)
    update_time: Optional[datetime]=Column(datetime, onupdate=datetime.utcnow)