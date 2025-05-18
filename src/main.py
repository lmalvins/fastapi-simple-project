# src/my_app/main.py
from fastapi import FastAPI

from api.books import router as books_router

app = FastAPI()

# Attach your routers here
app.include_router(books_router)