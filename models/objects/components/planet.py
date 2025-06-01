from models.objects.components.component import Component

class Planet(Component):
    def __init__(self, name:str, durability:int, cost:int, size:int, ores:list, atmosphere:int, galaxy):
        super().__init__(name, durability, cost)
        self.size = size
        self.ores = ores
        self.atmosphere = atmosphere
        self.galaxy = galaxy
        self.planethood = "By " + self.name 
