def greet():
    print('hello')


def before_and_after(func):
    print("before")
    func()
    print("after")


before_and_after(greet)
before_and_after(lambda :print(5))

def print_func(string):
    print(string)

#with parameters
before_and_after(lambda :print_func("123"))



boooks =[
    {"name": "book1", "author": "Lina"},
    {"name": "book2", "author": "Dengwei"},
    {"name": "book3", "author": "Lina"}
]

find_by = input("find the movie by ")
search_for = input("what are you looking for ")

def search(searcher):
    for book in boooks:
        if searcher(book) == search_for:
            print(book)

def searcher(book):
    if book[find_by] ==  search_for:
        print(book)

search(lambda book:book[find_by])