class Database:
    content = []

    @classmethod
    def insert(cls,data):
        cls.content.append(data)

    @classmethod
    def remove(cls,data):
        cls.content.remove(data)

    @classmethod
    def find(cls,finder):
        return [d for d in cls.content if finder(d)]

    @classmethod
    def display(cls):
        for d in cls.content:
            print(d)