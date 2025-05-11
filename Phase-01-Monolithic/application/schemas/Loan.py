from datetime import datetime
from pydantic import BaseModel
from application.schemas.Book import MiniBookResponse


class LoanAction(BaseModel):
    user_id:  int
    book_id:  int
    due_date: datetime

class LoanIdAction(BaseModel):
    loan_id: int

class LoanResponse(BaseModel):
    id: int
    user_id: int
    book_id:  int
    due_date:  datetime
    issue_date: datetime
    status: str

class ReturnResponse(BaseModel):
    id: int
    user_id: int
    book_id:  int
    due_date:  datetime
    issue_date: datetime
    status: str
    return_date: datetime

class StatusAction(BaseModel):
    status: str

class LoanOfUserResponse(BaseModel):
    loan_id: int
    miniBookResponse:  MiniBookResponse
    issue_date:  datetime
    due_date: datetime
    return_date:  datetime
    staus: str
