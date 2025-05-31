from abc import ABC

class Object(ABC):
    def __init__(self, name:str, durability:int, cost:int):
        self.name = name
        self.durability = durability
        self.cost = cost