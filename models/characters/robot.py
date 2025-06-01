from .character import Character
from models.objects.components.planet import Planet
from models.inventory import Inventory

class Robot(Character):
    def __init__(self, name:str, age:int, health:int, planet:Planet, inventory:Inventory, skills:list, languague:str, ia):
        super().__init__(name, age, health, planet, inventory, skills)
        self.ia = ia
        self.signal = 10
    
    def sync():
        pass