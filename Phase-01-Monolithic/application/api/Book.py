from fastapi import APIRouter
from application.crud.Book import Book
from application.schemas.Book import AddBookAction, AddBookResponse, BookResponse, BooksResponse, DeleteResponse, UpdateBookAction
from typing import List

router=APIRouter(prefix='',tags=['Book'])

book=Book()

@router.post("/addbook/", response_model=AddBookResponse)
def add(bookInfo: AddBookAction):
    return book.add(bookInfo)

@router.get("/getbooks/", response_model=List[BooksResponse])
def getBooks():
    return book.getBooks()

@router.get("/getbook/{id}", response_model=BookResponse)
def getBook(id):
    return book.getBook(id)

@router.put("/updatebook/{id}", response_model=BookResponse)
def update(updateInfo: UpdateBookAction):
    return book.update()

@router.delete("/deletebook/{id}", response_model=DeleteResponse)
def delete(id):
    return book.delete(id)

