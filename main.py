# main.py

import book
import user
import check
from models import Book, User

def print_separator():
    print("=" * 40)

def main_menu():
    print_separator()
    print("Welcome to the Library Management System")
    print_separator()
    print("1. Add Book")
    print("2. List Books")
    print("3. Delete Book")
    print("4. Add User")
    print("5. List Users")
    print("6. Delete User")
    print("7. Checkout Book")
    print("8. Exit")
    print_separator()

    choice = input("Enter your choice (1-8): ")
    return choice
#
def main():
    book_manager = book.BookManager()
    user_manager = user.UserManager()
    checkout_manager = check.CheckoutManager()
    try:

        while True:
            choice = main_menu()
            print_separator()

            if choice == '1':
                print("Add a New Book")
                print_separator()
                title = input("Enter the title of the book: ")
                author = input("Enter the author of the book: ")
                isbn = input("Enter the ISBN of the book: ")
                book_manager.add_book(title, author, isbn)
                print("Book added successfully!")
            elif choice == '2':
                print("List of Books")
                print_separator()
                book_manager.list_books()
            elif choice == '3':
                print("Delete a Book")
                print_separator()
                isbn = input("Enter the ISBN of the book to delete: ")
                book_manager.delete_book(isbn)
                print("Book deleted successfully!")
            elif choice == '4':
                print("Add a New User")
                print_separator()
                name = input("Enter the name of the user: ")
                user_id = input("Enter the ID of the user: ")
                user_manager.add_user(name, user_id)
                print("User added successfully!")
            elif choice == '5':
                print("List of Users")
                print_separator()
                user_manager.load_users()
            elif choice == '6':
                print("Delete a User")
                print_separator()
                user_id = input("Enter the ID of the user to delete: ")
                user_manager.delete_user(user_id)
                print("User deleted successfully!")
            elif choice == '7':
                print("Checkout a Book")
                print_separator()
                user_id = input("Enter your user ID: ")
                isbn = input("Enter the ISBN of the book to checkout: ")
                checkout_manager.checkout_book(user_id, isbn)
                print("Book checked out successfully!")
            elif choice == '8':
                print("Exiting the Library Management System. Goodbye!")
                break
            else:
                print("Invalid choice! Please try again.")
    except:
        print("error in code")
            

if __name__ == "__main__":
    main()
    
