class Book:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year
        self.IsRead = False

    def __repr__(self):
        return f'<Book {self.name}, Author {self.author}, Release year {self.year}>, Is Read {self.IsRead}'

# class SingletonConstructionError(Exception):
#     print("please use .Create Construction")


# class BookStore:
#     __isInstant = None
#     def __init__(self):
#         raise SingletonConstructionError
#
#     @classmethod
#     def CreateBookStore(cls):
#         if BookStore._isInstant is not None:
