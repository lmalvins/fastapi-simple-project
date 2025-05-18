from fastapi import FastAPI, APIRouter

from fastapi_simple_project.services.book_service import BookService

router = APIRouter()
book_service = BookService()

@router.get("/books")
def get_books():
    return book_service.get_books()