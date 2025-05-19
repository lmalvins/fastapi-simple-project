# src/my_app/main.py
from fastapi import FastAPI

from src.api.books import router as books_router

app = FastAPI()

app.include_router(books_router)
