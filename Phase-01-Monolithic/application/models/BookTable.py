from sqlalchemy import  Column, Integer, String, Metadata, Table
from datetime  import  datetime


class BookTable(Base):
    __tablename__='book'
    book_id=Column(Integer, primary_key=True)
    book_title=Column(String, unique=True)
    author=Column(String)
    isbn=Column(String, unique=True)
    copies=Column(Integer)
    available_copies=Column(Integer)
    creation_time=Column(datetime)
    update_time=Column(datetime)



