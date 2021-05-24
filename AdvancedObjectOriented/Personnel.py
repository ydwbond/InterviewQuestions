from AdvancedObjectOriented.Savable import Savable
from AdvancedObjectOriented.Database import Database


class Personnel(Savable):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"<name {self.name}>"

    def save(self):
        Database.insert(self)
