"""
store and retrieving books from a list
"""

import PythonWithDatabase.Utility.Database as DB
import PythonWithDatabase.Utility.InmemoryStore as IS
import PythonWithDatabase.Utility.CsvFiles as FL
import PythonWithDatabase.Utility.JsonFiles as JF

USER_CHOICE = """
- 'a' to add a book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- q' to quit

You choice:"""

ACTION = {
    "a":DB.prompt_add_book,
    "l":DB.list_book,
    "r":DB.prompt_mark_book_read,
    "d":DB.prompt_delete_book
}

def manu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        ACTION[user_input]()
        user_input = input(USER_CHOICE)

manu()