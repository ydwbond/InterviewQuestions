from abc import ABCMeta, abstractmethod


class Savable(metaclass=ABCMeta):

    @abstractmethod
    def save(self):
        pass
