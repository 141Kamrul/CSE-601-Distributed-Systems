from sqlalchemy import  Column, Integer, String, Metadata, Table
from  datatime import datatime

class LoanTable(Base):
    __tablename__='loan'
    loan_id=Column(Integer, primary_key=True)
    user_id=Column(Integer,  foreign_key=True)
    book_id=Column(Integer,  foreign_key=True)
    issue_time=Column(datetime)
    due_time=Column(datetime)
    return_time=Column(datetime)
    extended_time=Column(datetime)
    extended_count=Column(Integer)
    



