from fastapi  import HTTPException
from application.schemas.Loan import LoanResponse, LoanAction, LoanIdAction, ReturnResponse, StatusAction, LoanOfUserResponse, ReturnTimeAction, OverdueLoanResponse, ExtendedLoanResponse
from application.models.Loan import Loan as LoanTable
from application.database.Session import session_instance
from typing import List
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime, timezone
from application.crud.User import User
from application.crud.Book import Book

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
        updatedReturnTime=ReturnTimeAction(return_time=timezone.utc)
        updatedLoan=session_instance.update(LoanTable,loanId.loan_id,updatedStatus,updatedReturnTime)

        
        return ReturnResponse(
                id=updatedLoan.id,
                user_id=updatedLoan.user_id,
                book_id=updatedLoan.book_id,
                issue_date=updatedLoan.issue_time,
                due_date=updatedLoan.original_due_time,
                return_date=updatedLoan.return_time,
                status=updatedLoan.status
            )
        
    
    def getLoansUser(self, id) -> List[LoanOfUserResponse]:
        loans=session_instance.read_filter_all(LoanTable, user_id=id)
        loanResponses=[]
        for loan in loans:
            book=Book()
            loanResponses.append(LoanOfUserResponse(
                loan_id=loan.id,
                miniBookResponse=book.getMiniBook(id),
                issue_date=loan.issue_time,
                due_date=loan.original_due_time,
                return_date=loan.return_time,
                status=loan.status,
            ))
        return loanResponses

    def getOverdueLoans(self) -> List[OverdueLoanResponse]:
        loans=session_instance.read_filter_all(LoanTable, status="ACTIVE")
        user=User()
        book=Book()
        overDueLoans=[]
        for loan in loans:
            overDueLoans.append(
                OverdueLoanResponse(
                    loan_id=loan.id,
                    miniUserResponse=user.getMiniUser(loan.user_id),
                    miniBookResponse=book.getMiniBook(loan.book_id),
                    issue_date=loan.issue_time,
                    due_date=loan.original_due_time,
                    days_overdue=datetime.utcnow-loan.original_due_time
                )
            )
        return overDueLoans

    def extendUserLoan(self, id, extendInfo) -> ExtendedLoanResponse:
        loan=session_instance.read_one(id)
        updatedLoan=session_instance.update(LoanTable, id, extendInfo)
        return ExtendedLoanResponse(
            loan_id=updatedLoan.id,
            user_id=updatedLoan.user_id,
            book_id=updatedLoan.book_id,
            issue_date=updatedLoan.issue_time,
            original_due_date=updatedLoan.original_due_time,
            extended_due_date=datetime,
            status=updatedLoan.status,
            extension_count=int
        )

