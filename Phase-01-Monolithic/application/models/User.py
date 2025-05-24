from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from application.database.Base import Base


class User(Base):
    __tablename__='users'
    id: int=Column(Integer,primary_key=True)
    name: str=Column(String(30),unique=True,nullable=False)
    email: str=Column(String(30),nullable=False)
    role: str=Column(String(20),nullable=False)
    books_borrowed: int=Column(Integer, default=0)
    current_borrows: int=Column(Integer, default=0)