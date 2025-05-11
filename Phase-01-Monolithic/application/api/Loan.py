from fastapi import APIRouter
from application.crud.Loan import Loan
from application.schemas.Loan import LoanAction, LoanResponse, ReturnResponse,  LoanIdAction,LoanOfUserResponse
from typing import List

router=APIRouter(prefix='',tags=['Loan'])

loan=Loan()

@router.post("/loan/", response_model=LoanResponse)
def issueloan(loanInfo: LoanAction):
    return loan.issueloan(loanInfo)


@router.post("/returns/", response_model=ReturnResponse)
def returns(loanId: LoanIdAction):
    return loan.returns(loanId)

@router.get("loans/{user_id}",  response_model=List[LoanOfUserResponse])
def getUserLoans(user_id):
    return loan.getUserLoans(user_id)

@router.get("loans/overdue",  response_model=List[LoanOfUserResponse])
def getUserLoans(user_id):
    return loan.getUserLoans(user_id)

@router.put("loans/{id}/extend",  response_model=List[LoanOfUserResponse])
def getUserLoans(user_id):
    return loan.getUserLoans(user_id)