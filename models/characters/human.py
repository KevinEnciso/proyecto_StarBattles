from .alive import Alive
from models.objects.components.planet import Planet
from models.inventory import Inventory

class Human(Alive):
    def __init__(self, name:str, age:int, health:int, planet:Planet, inventory:Inventory, skills:list, intelligence:int):
        super().__init__(name, age, health, planet, inventory, skills,  intelligence)
    
    def eat():
        pass
    
    def talk(self):
        pass

    def die(self):
        pass