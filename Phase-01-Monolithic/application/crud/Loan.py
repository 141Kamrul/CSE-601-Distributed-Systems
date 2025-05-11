from fastapi  import HTTPException
from application.schemas.Loan import LoanResponse, LoanAction, LoanIdAction, ReturnResponse, StatusAction, LoanOfUserResponse
from application.models.Loan import Loan as LoanTable
from application.database.Session import session_instance
from typing import List
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime, timezone
from application.crud.User import User

class Loan:

    def issueloan(self, loanInfo: LoanAction) -> LoanResponse:
        try:
            loan=LoanTable(user_id=loanInfo.user_id,
                           book_id=loanInfo.book_id,
                           original_due_time=loanInfo.due_date
                        )
            session_instance.write(loan)
            #session_instance.refresh(loan)
            return LoanResponse(
                id=loan.id,
                user_id=loan.user_id,
                book_id=loan.book_id,
                issue_date=loan.issue_time,
                due_date=loan.original_due_time,
                status=loan.status
            )
            
        except SQLAlchemyError as e:
            raise HTTPException(status_code=500, detail="Database error while issuing loan")
        except Exception as e:
            raise HTTPException(status_code=500, detail="Unexpected error while issuing loan")


    def returns(self,  loanId: LoanIdAction) -> ReturnResponse:
        loan=session_instance.read_one(LoanTable, loanId.loan_id)
        updatedStatus=StatusAction(status="RETURNED")
        updatedLoan=session_instance.update(LoanTable,loanId.loan_id,updatedStatus)

        
        return ReturnResponse(
                id=updatedLoan.id,
                user_id=updatedLoan.user_id,
                book_id=updatedLoan.book_id,
                issue_date=updatedLoan.issue_time,
                due_date=updatedLoan.original_due_time,
                return_date=datetime.now(timezone.utc),
                status=updatedLoan.status
            )
        
    
    def getUserLoans(self, id) -> List[LoanOfUserResponse]:
        user=User()
        user=user.getUser(id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return UserResponse(
            name=user.username,
            email=user.email,
            role=user.role
        )