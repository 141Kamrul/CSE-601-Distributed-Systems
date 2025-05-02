from fastapi import HTTPException
from application.schemas.Book import AddBookAction, AddBookResponse, BookResponse, BooksResponse, DeleteResponse, UpdateBookAction
from application.models.Book import Book as BookTable
from application.database.Session import session_instance
from typing import List

class Book:

    def add(self, bookInfo: AddBookAction) -> AddBookResponse:
        try:
            book=BookTable(title=bookInfo.title,
                           author=bookInfo.author,
                           isbn=bookInfo.isbn,
                           copies=bookInfo.copies
                        )
            session_instance.write(book)
            return AddBookResponse(message="Book added succesfully")
        except:
            return AddBookResponse(message="Addition failed")

    def getBooks(self) -> List[BooksResponse]:
        books=session_instance.read_all(BookTable)
        print(books)
        booksResponses=[]
        for book in books:
            bookResponses.append(
                BookResponse(
                    book_id=book.id,
                    title=book.title,
                    author=book.author,
                    isbn=book.isbn,
                    copies=book.copies,
                )
            )
        return booksResponses

    def getBook(self, id) -> BookResponse:
        book=session_instance.read_one(BookTable,id)
        if not book:
            raise HTTPException(status_code=404, detail="Book not found")
        return BookResponse(
            title=book.title,
            author=book.author,
            isbn=book.isbn,
            copies=book.copies,
            available_copies=book.available_copies,
            created_at=book.creation_time,
            updated_at=book.update_time
        )

    def updateBook(self, id, updateInfo) -> BookResponse:
        book=session_instance.read_one(BookTable,id)
        if not book:
            raise HTTPException(status_code=404, detail="Book not found")
        updatedBook=session_instance.update(BookTable, id, updateInfo)
        return BookResponse(
            title=updatedBook.title,
            author=updatedBook.author,
            isbn=updatedBook.isbn,
            copies=updatedBook.copies,
            available_copies=updatedBook.available_copies,
            created_at=updatedBook.creation_time,
            updated_at=updatedBook.update_time
        )

    def deleteBook(self,  id) -> DeleteResponse:
        if session_instance.delete(BookTable, id):
            return DeleteResponse(message="Book deleted successfully")
        else:
            return DeleteResponse(message="Book not found")