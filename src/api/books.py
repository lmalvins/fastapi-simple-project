from fastapi import APIRouter

from src.services.book_service import BookService

router = APIRouter()
book_service = BookService()

@router.get("/books")
def get_books():
    return book_service.get_books()