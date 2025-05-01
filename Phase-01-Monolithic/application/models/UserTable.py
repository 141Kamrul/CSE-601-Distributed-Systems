from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from  typing  import Optional

Base=declarative_base()

class UserTable(Base):
    __tablename__='user'
    user_id=Column(Integer, primary_key=True)
    user_name=Column(String, unique=True)
    email=Column(String, unique=True)
    role=Column(int)