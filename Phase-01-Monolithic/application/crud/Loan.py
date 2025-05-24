from fastapi  import HTTPException
from application.schemas.Loan import LoanResponse, LoanAction, LoanIdAction, ReturnResponse, ReturnUpdateAction, LoanOfUserResponse, OverdueResponse, ExtendedLoanResponse, UpdateLoanAction
from application.schemas.Book import UpdateBookAction
from application.models.Loan import Loan as LoanTable
from application.database.Session import session_instance
from typing import List
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime, timezone, timedelta
from application.crud.User import User
from application.crud.Book import Book

class Loan:

    def issueloan(self, loanInfo: LoanAction) -> LoanResponse:
        loan=LoanTable(user_id=loanInfo.user_id,
                        book_id=loanInfo.book_id,
                        original_due_date=loanInfo.due_date
                    )
        session_instance.write(loan)
        if loan:
            user=User()
            user.loanNumber(loan.user_id, 1, 1)
            book=Book()
            book.updateBookCopy(loan.book_id,-1)

            return LoanResponse(
                id=loan.id,
                user_id=loan.user_id,
                book_id=loan.book_id,
                issue_date=loan.issue_date,
                due_date=loan.original_due_date,
                status=loan.status
            )

        raise HTTPException(status_code=500, detail="Database error while issuing loan")


    def returns(self,  loanId: LoanIdAction) -> ReturnResponse:
        loan=session_instance.read_one(LoanTable, loanId.loan_id)
        updates=ReturnUpdateAction(
            status="RETURNED",
            return_date=datetime.now(timezone.utc)
        )
    
        updatedLoan=session_instance.update(LoanTable,loanId.loan_id,updates)

        if not updatedLoan:
            raise HTTPException(status_code=500, detail="Database error while issuing loan")
        
        user=User()
        user.loanNumber(loan.user_id, -1, 0)
        book=Book()
        book.updateBookCopy(loan.book_id, 1)

        return ReturnResponse(
                id=updatedLoan.id,
                user_id=updatedLoan.user_id,
                book_id=updatedLoan.book_id,
                issue_date=updatedLoan.issue_date,
                due_date=updatedLoan.original_due_date,
                return_date=updatedLoan.return_date,
                status=updatedLoan.status
            )
        
    
    def getLoansUser(self, user_id) -> List[LoanOfUserResponse]:
        loans=session_instance.read_filter_all(LoanTable, user_id=user_id)
        loanResponses=[]
        for loan in loans:
            book=Book()
            loanResponses.append(
                LoanOfUserResponse(
                    id=loan.id,
                    book=book.getMiniBook(loan.book_id),
                    issue_date=loan.issue_date,
                    due_date=loan.original_due_date,
                    return_date=loan.return_date,
                    status=loan.status,
                )
            )
        return loanResponses


    def getAllOverdueLoans(self) -> List[OverdueResponse]:
        loans=session_instance.read_filter_all(LoanTable,status="ACTIVE")
        user=User()
        book=Book()
        overDueLoans=[]
        for loan in loans:
            due_date=loan.extended_due_date if loan.extended_due_date else loan.original_due_date

            days_overdue=(datetime.utcnow().date()-due_date.date()).days
            if days_overdue<0:
                continue
                
            overDueLoans.append(
                OverdueResponse(
                    id=loan.id,
                    user=user.getMiniUser(loan.user_id),
                    book=book.getMiniBook(loan.book_id),
                    issue_date=loan.issue_date,
                    due_date=due_date,
                    days_overdue=days_overdue
                )
            )
        return overDueLoans

    def extendUserLoan(self, id, extendInfo) -> ExtendedLoanResponse:
        loan=session_instance.read_one(LoanTable, id)

        base_date = loan.extended_due_date if loan.extended_due_date else loan.original_due_date

        updateInfo=UpdateLoanAction(
            extension_days=extendInfo.extension_days,
            extensions_count=loan.extension_count+1,
            extended_due_date=base_date+timedelta(days=extendInfo.extension_days) 
        )
        updatedLoan=session_instance.update(LoanTable, id, updateInfo)

        return ExtendedLoanResponse(
            id=updatedLoan.id,
            user_id=updatedLoan.user_id,
            book_id=updatedLoan.book_id,
            issue_date=updatedLoan.issue_date,
            original_due_date=updatedLoan.original_due_date,
            extended_due_date=updatedLoan.extended_due_date,
            status=updatedLoan.status,
            extensions_count=updatedLoan.extension_count
        )

    def getTotalOverdueLoans(self):
        loans=session_instance.read_all(LoanTable)
        count=0
        for loan in loans:
            if loan.status=="ACTIVE":
                count+=1
        return count

    def getLoansToday(self):
        loans=session_instance.read_all(LoanTable)
        count=0
        for loan in loans:
            if loan.issue_time.date()==datetime.utcnow().date():
                count+=1
        return count

    def getReturnsToday(self):
        loans=session_instance.read_all(LoanTable)
        count=0
        for loan in loans:
            if loan.return_time.date()==datetime.utcnow().date():
                count+=1
        return count

    def getActiveUsers(self):
        loans=session_instance.read_filter_all(LoanTable)
        user_stats = defaultdict(lambda: {
            "books_borrowed": 0,
            "current_borrows": 0
        })
    
    
        for loan in all_loans:
            user_stats[loan.user_id]["books_borrowed"] += 1
            if loan.status == "ACTIVE":
                user_stats[loan.user_id]["current_borrows"] += 1
    
        sorted_users = sorted(
            user_stats.items(),
            key=lambda x: x[1]["current_borrows"],
            reverse=True
        )
    
        return dict(sorted_users)


