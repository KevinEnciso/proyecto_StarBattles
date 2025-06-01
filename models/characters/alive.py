from .character import Character
from models.objects.components.planet import Planet
from models.inventory import Inventory
from abc import abstractmethod

class Alive(Character):
    def __init__(self, name:str, age:int, health:int, planet:Planet, inventory:Inventory, skills:list, intelligence:int):
        super().__init__(name, age, health, planet, inventory, skills)
        self.hunger = 0
        self.sanity = 100
        self.intelligence = intelligence

    @abstractmethod
    def eat():
        pass
    