from fastapi import APIRouter, HTTPException

from src.services.book_service import BookService

router = APIRouter()
book_service = BookService()

@router.get("/books")
def get_books():
    return book_service.get_books()

@router.get("/books/{book_title}")
def get_books(book_title: str):
    for book in book_service.get_books():
        if book.title.casefold() == book_title.casefold():
            return book
    raise HTTPException(status_code=404, detail="Book not found")
