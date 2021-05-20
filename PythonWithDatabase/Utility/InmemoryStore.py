from PythonWithDatabase.Utility.Book import Book

import logging

logger = logging.getLogger("test")

book_list = []

def prompt_add_book():
    book_name = input("Please enter a book name")
    book_author = input("Please input the author of the book")
    book_year = input("Please input the the year book release")
    b1 = search_book(book_name)
    if b1 is None:
        book_list.append(Book(book_name, book_author, book_year))
    else:
        print(f"the book {book_name} is already in your collection")


def list_book():
    for book in book_list:
        print(book)


def prompt_mark_book_read():
    book_name = input("Please enter the book name")
    b1 = search_book(book_name)
    if b1 is None:
        print(f"the book {book_name} is not found in  your collection")
    else:
        b1.IsRead = True


def prompt_delete_book():
    book_name = input("Please enter the book name")
    b = search_book(book_name)
    if b is not None:
        delete_book(b)
    else:
        print(f"the book {book_name} is not found in  your collection")


def search_book(book_name):
    for book in book_list:
        if book.name == book_name:
            return book
            break
    else:
        return None


def delete_book(book):
    book_list.remove(book)




