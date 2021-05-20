from PythonWithDatabase.Utility.Book import Book
import logging
from os import path

logger = logging.getLogger("test")

book_store_file = r"C:\Users\Dengwei\Dropbox\Job Hunting\Study\Python\InterViewQuestion\PythonWithDatabase\Utility\book_list.csv"

book_list_mem_cache = []


def prompt_add_book():
    book_name = input("Please enter a book name")
    book_author = input("Please input the author of the book")
    book_year = input("Please input the the year book release")
    b1 = search_book(book_name)
    if b1 is None:
        book_list_mem_cache.append(Book(book_name, book_author, book_year))
        _push_book_mem_cache_to_file()
    else:
        print(f"the book {book_name} is already in your collection")


def list_book():
    for book in book_list_mem_cache:
        print(book)


def prompt_mark_book_read():
    book_name = input("Please enter the book name")
    b1 = search_book(book_name)
    if b1 is None:
        print(f"the book {book_name} is not found in  your collection")
    else:
        b1.IsRead = True
        _push_book_mem_cache_to_file()


def prompt_delete_book():
    book_name = input("Please enter the book name")
    b = search_book(book_name)
    if b is not None:
        delete_book(b)
        _push_book_mem_cache_to_file()
    else:
        print(f"the book {book_name} is not found in  your collection")


def search_book(book_name):
    for book in book_list_mem_cache:
        if book.name == book_name:
            return book
            break
    else:
        return None


def _refresh_book_mem_cache():
    if path.exists(book_store_file):
        with open(book_store_file, 'r') as book_file:
            file_string = book_file.read()
            if file_string != "":
                books_as_list = [book.strip().split(',') for book in file_string.split('\n')]
                global book_list_mem_cache
                book_list_mem_cache = [ ]  # clear all the cache
                for book_list in books_as_list:
                    if len(book_list) > 1:
                        book = Book(book_list[ 0 ], book_list[ 1 ], book_list[ 2 ])
                        book.IsRead = True if book_list[ 3 ] != 0 else False
                        book_list_mem_cache.append(book)
    else:
        with open(book_store_file, 'w'):
            pass

def _push_book_mem_cache_to_file():
    long_string_book = ""
    for book in book_list_mem_cache:
        long_string_book += book.name + "," + book.author + "," + book.year + "," + ("1" if book.IsRead else "0") + "\n"
    with open(book_store_file, 'w') as book_file:
        book_file.write(long_string_book)


def delete_book(book):
    book_list_mem_cache.remove(book)

if __name__ == "__main__":
    with open(book_store_file, 'r') as book_file:
        print(book_file.read())
_refresh_book_mem_cache() #need to run this at the begining of the programe