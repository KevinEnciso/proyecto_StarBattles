from ..object import Object
from abc import abstractmethod

class Item(Object):
    @abstractmethod
    def use(self):
        pass