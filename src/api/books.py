from fastapi import APIRouter, HTTPException, Body

from domain.book import Book
from src.services.book_service import BookService

router = APIRouter()
book_service = BookService()

@router.get("/books")
def get_all_books():
    return book_service.get_books()

@router.get("/books/{book_title}")
def get_books_by_title(book_title: str):
    for book in book_service.get_books():
        if book.title.casefold() == book_title.casefold():
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@router.get("/books/")
def get_books_by_category(category: str):
    book_list = []
    for book in book_service.get_books():
        if book.category.casefold() == category.casefold():
            book_list.append(book)
    return book_list

@router.get("/books/{book_author}/")
def get_books_by_category_author(category: str, book_author: str):
    book_list = []
    for book in book_service.get_books():
        if book.category.casefold() == category.casefold() and book.author.casefold() == book_author.casefold():
            book_list.append(book)
    return book_list

@router.post("/books")
def post_books(book_request_body: Book):
    new_book=Book(**book_request_body.model_dump())
    book_service.add_book(new_book)

@router.put("/books")
def put_books(updated_book=Body()):
    for i in range (len(book_service.get_books())):
        if book_service.get_books()[i].title.casefold() == updated_book.get('title').casefold():
            book_service.get_books()[i] = updated_book
