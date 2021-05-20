from PythonWithDatabase.Utility.Book import Book
import logging
from os import path
from PythonWithDatabase.Utility.Connection import Connection

db_file = r"C:\Users\Dengwei\Dropbox\Job Hunting\Study\Python\InterViewQuestion\PythonWithDatabase\Utility\book_list.db"


def _set_up_database():
    if not path.exists(db_file):
        with open(db_file,'w'):
            pass
    with Connection(db_file) as conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS books (name text primary key, author text, read integer)")


def prompt_add_book():
    book_name = input("Please enter a book name ")
    book_author = input("Please input the author of the book ")
    with Connection(db_file) as conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO books VALUES (?,?,0)",(book_name,book_author))


def list_book():
    with Connection(db_file) as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM books")
        rows = cur.fetchall()
        for row in rows:
            print(f"book name {row[0]}, Author {row[1]}, is ready {row[2]}")


def prompt_mark_book_read():
    book_name = input("Please enter the book name")
    with Connection(db_file) as conn:
        cur = conn.cursor()
        cur.execute("UPDATE books set read = 1 where name = ?",(book_name,))



def prompt_delete_book():
    book_name = input("Please enter the book name")
    with Connection(db_file) as conn:
        cur = conn.cursor()
        cur.execute("DELETE from books where name = ?",(book_name,))


_set_up_database()