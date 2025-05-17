from application.schemas.Stats import PopularBookResponse, ActiveUserResponse, OverviewResponse
from application.crud.User import User
from application.crud.Book import Book
from application.crud.Loan import Loan
from typing import List

class Stats:
    def getPopularBooks() -> List[PopularBookResponse]:
        book=Book()
        books=book.getMiniBook()
        popularBooks=[]
        for book in books:
            popularBooks.append(
                PopularBookResponse(
                    book_id=book.id,
                    title=book.title,
                    author=book.author,
                    borrow_count=book.copies-book.available_copies
                )
            )
        return popularBooks

    def getActiveUsers() -> List[ActiveUserResponse]:
        loan=Loan()
        user=User()
        activeUsers=loan.getActiveUsers()
        mostActiveUsers=[]

        for user_id, stats in activeUsers.items():  
            mostActiveUsers.append(
                ActiveUserResponse(
                    user_id=user_id, 
                    name=user.getUsername(user_id),  
                    books_borrowed=stats["books_borrowed"],  
                    current_borrows=stats["current_borrows"]  
                )
            )
        return mostActiveUsers

    def getOverview() -> OverviewResponse:
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