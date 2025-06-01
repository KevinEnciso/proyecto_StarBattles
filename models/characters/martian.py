from .alive import Alive
from models.objects.components.planet import Planet
from models.inventory import Inventory

class Martian(Alive):
    def __init__(self, name:str, age:int, health:int, planet:Planet, inventory:Inventory, skills:list, languague:str, intelligence:int):
        super().__init__(name, age, health, planet, inventory, skills, intelligence)