from typing import List

from src.domain.book import Book


class BookService:

    BOOKS= [Book(title="Title One", author="Author One", category="Science"),
            Book(title="Title Two", author="Author Two", category="Fiction"),
            Book(title="Title Three", author="Author Three", category="Adventure"),
            Book(title="Title Four", author="Author Four", category="Terror"),
            Book(title="Title Five", author="Author Five", category="Terror"),]

    def get_books(self) -> List[Book]:
        return self.BOOKS

    def add_book(self, book):
        self.BOOKS.append(book)
