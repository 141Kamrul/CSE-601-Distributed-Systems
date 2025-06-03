from application.schemas.Stats import PopularBookResponse, ActiveUserResponse, OverviewResponse
from application.crud.User import User
from application.crud.Book import Book
from application.crud.Loan import Loan
from typing import List

class Stats:
    def getPopularBooks(self) -> List[PopularBookResponse]:
        book=Book()
        popularBooks=book.getMiniBooks()
        popularBooks.sort(key=lambda x: x.borrow_count, reverse=True)
        return popularBooks

    def getActiveUsers(self) -> List[ActiveUserResponse]:
        user=User()
        mostActiveUsers=user.getActiveUsers()
        mostActiveUsers.sort(key=lambda x: x.books_borrowed, reverse=True)
        return mostActiveUsers

    def getOverview(self) -> OverviewResponse:
        book=Book()
        user=User()
        loan=Loan()
        return OverviewResponse(
            total_books=book.getTotalBooks(),
            total_users=user.getTotalUser(),
            books_available=book.getTotalAvailableBooks(),
            books_borrowed=book.getTotalBorrowedBooks(),
            overdue_loans=loan.getTotalOverdueLoans(),
            loans_today=loan.getLoansToday(),
            returns_today=loan.getReturnsToday()
        )