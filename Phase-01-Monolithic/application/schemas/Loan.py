from datetime import datetime
from pydantic import BaseModel
from application.schemas.Book import MiniBookResponse
from application.schemas.User import MiniUserResponse


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
    return_date: datetime | None

class ReturnUpdateAction(BaseModel):
    status: str
    return_time: datetime | None

class LoanOfUserResponse(BaseModel):
    loan_id: int
    miniBookResponse: MiniBookResponse
    issue_date: datetime
    due_date: datetime
    return_date: datetime | None
    status: str

class OverdueLoanResponse(BaseModel):
    loan_id: int
    miniUserResponse: MiniUserResponse
    miniBookResponse: MiniBookResponse
    issue_date: datetime
    due_date: datetime
    days_overdue: datetime

class ExtendedLoanResponse(BaseModel):
    loan_id: int
    user_id: int
    book_id: int
    issue_date: datetime
    original_due_date: datetime
    extended_due_date: datetime | None
    status: str
    extension_count: int

class ExtendLoanAction(BaseModel):
    extended_days: int
