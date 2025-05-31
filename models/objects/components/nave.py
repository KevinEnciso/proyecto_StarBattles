from models.objects.components.component import Component
from models.inventory import Inventory

class Nave(Component):
    def __init__(self, name:str, durability:int, cost:int, energy:int, size:int, crew:list, velocity:float, components:list, inventory:Inventory):
        super().__init__(name, durability, cost)
        self.energy = energy
        self.size = size
        self.crew = crew
        self.velocity = velocity
        self.components = components
        self.inventory = inventory