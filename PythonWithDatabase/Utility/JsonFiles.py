"""
save the data in a Json file
[
    {
        "name": "book1",
        "author": "lina"
        "read" : True
    }
]
"""
from os import path
import json

json_file = r"C:\Users\Dengwei\Dropbox\Job Hunting\Study\Python\InterViewQuestion\PythonWithDatabase\Utility\book_list.json"
in_mem_book_list_json = []


def _populate_in_mem_book():
    if not path.exists(json_file):
        with open(json_file,'w') as file:
            json.dump([],file)
    else:
        with open(json_file,'r') as file:
            global in_mem_book_list_json
            in_mem_book_list_json= json.load(file)


def _save_to_file():
    with open(json_file, 'w') as file:
        json.dump(in_mem_book_list_json, file)


def prompt_add_book():
    book_name = input("Please enter a book name ")
    book_author = input("Please input the author of the book ")
    in_mem_book_list_json.append({"name": book_name, "author": book_author, "read": False})
    _save_to_file()


def list_book():
    for book in in_mem_book_list_json:
        read = 'YES' if book['read'] else 'NO'
        print(f"book name {book['name']}, bool author {book['author']}, Is read {read}")


def prompt_mark_book_read():
    book_name = input("Please enter a book name ")
    for book in in_mem_book_list_json:
        if book['name'] == book_name:
            book['read'] = True
    _save_to_file()


def prompt_delete_book():
    book_name = input("Please enter a book name ")
    for book in in_mem_book_list_json:
        if book['name'] == book_name:
            in_mem_book_list_json.remove(book)
    _save_to_file()

_populate_in_mem_book()