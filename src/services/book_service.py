from typing import List

from src.domain.book import Book


class BookService:

    BOOKS= [Book(id="1", title="Title One", author="Author One", category="Science"),
            Book(id="2",title="Title Two", author="Author Two", category="Fiction"),
            Book(id="3",title="Title Three", author="Author Three", category="Adventure"),
            Book(id="4",title="Title Four", author="Author Four", category="Terror"),
            Book(id="5",title="Title Five", author="Author Five", category="Terror"),]

    def get_books(self) -> List[Book]:
        return self.BOOKS

    def add_book(self, book):
        self.BOOKS.append(book)
