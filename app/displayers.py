from abc import ABC, abstractmethod

from app.main import Book


class BookDisplayer(ABC):
    @abstractmethod
    def display(self, content: str) -> None:
        pass


class ConsoleDisplayer(BookDisplay):
    def display(self, book: Book) -> None:
        print(book.content)


class ReverseDisplayer(BookDisplay):
    def display(self, book: Book) -> None:
        print(book.content[::-1])
