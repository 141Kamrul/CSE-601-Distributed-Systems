from pydantic  import BaseModel
from datetime import  datetime

class AddBookAction(BaseModel):
    title: str
    author: str
    isbn: str
    copies: int

class AddBookResponse(BaseModel):
    message:  str

class BookResponse(BaseModel):
    title: str
    author: str
    isbn: str
    copies: int
    available_copies: int
    created_at: datetime
    updated_at: datetime

class BooksResponse(BaseModel):
    book_id: int
    title: str
    author: str
    isbn: str
    copies: int

class UpdateBookAction(BaseModel):
    copies: int
    available_copies: int

class DeleteResponse(BaseModel):
    message: str

class MiniBookResponse(BaseModel):
    book_id: int
    title: str
    author: str