# models.py
#crearing models for our library management system
#implementation of the concept of constructors and encapsulation of our data, function useed inside abstract class will be used in rest of our files
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
    #use of pythonic code, implementing book authors in dictionary format with unique isbn code; this isbn code will help in using crud operations on local storage
    def to_dict(self):
        return {"title": self.title, "author": self.author, "isbn": self.isbn}

class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
     #use of pythonic code, implementing users in dictionary format with unique isbn code; this isbn code will help in using crud operations on local storage
    def to_dict(self):
        return {"name": self.name, "user_id": self.user_id}

class Checkout:
    def __init__(self, user_id, isbn):
        self.user_id = user_id
        self.isbn = isbn

    def to_dict(self):
        return {"user_id": self.user_id, "isbn": self.isbn}
