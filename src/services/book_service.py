from typing import List

from domain.book import Book


class BookService:
    def get_books(self) -> List[Book]:
        return [
            Book(title="Title One", author="Author One", category="Science"),
            Book(title="Title Two", author="Author Two", category="Fiction"),
        ]