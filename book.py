# book.py

from models import Book
import storage
#Represents a book in the library.
    
    # Attributes:
    #     title (str): The title of the book.
    #     author (str): The author of the book.
    #     isbn (str): The ISBN (International Standard Book Number) of the book.
    
class BookManager:
    def __init__(self):
        self.books = []
#function to add book
    def add_book(self, title, author, isbn):
        new_book = Book(title, author, isbn)
        self.books.append(new_book)
        self._save_books()
#function to delete book

#  """Add a new book to the library.

#     Args:
#         title (str): The title of the book.
#         author (str): The author of the book.
#         isbn (str): The ISBN of the book.

#     Raises:
#         BookError: If an error occurs while adding the book.
#     """
  
    def delete_book(self, isbn):
        self.books = [book for book in self.books if book.isbn != isbn]
        self._save_books()
#function to save book
    def _save_books(self):
        data = [book.to_dict() for book in self.books]
        storage.save_to_file(data, "books.json")
#function to load book
    def load_books(self):
        data = storage.load_from_file("books.json")
        self.books = [Book(book['title'], book['author'], book['isbn']) for book in data]
#function to list all the listed books
    def list_books(self):
        self.load_books()
        for book in self.books:
            print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}")
