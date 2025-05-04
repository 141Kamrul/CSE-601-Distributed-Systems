from fastapi import APIRouter
from application.crud.Loan import Loan
from application.schemas.Loan import LoanAction, LoanResponse, ReturnResponse,  LoanIdAction, StatusAction
from typing import List

router=APIRouter(prefix='',tags=['Loan'])

loan=Loan()

@router.post("/loan/", response_model=LoanResponse)
def issueloan(loanInfo: LoanAction):
    return loan.issueloan(loanInfo)


@router.post("/returns/", response_model=ReturnResponse)
def returns(loanId: LoanIdAction, sta:StatusAction):
    return loan.returns(loanId)
'''
@router.get("/getuser/{id}",  response_model=UserResponse)
def getUser(id):
    return user.getUser(id)'''