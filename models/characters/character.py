from abc import ABC, abstractmethod
from models.inventory import Inventory
from models.objects.components.planet import Planet

class Character(ABC):
    def __init__(self, name: str, age: int, health: int, planet: Planet, inventory: Inventory, skills:list):
        self.name = name
        self.age = age
        self.health = health
        self.planet = planet
        self.planethood = self.planet.planethood
        self.inventory = inventory
        self.skills = skills
        self.languague = self.planet.planethood

    @abstractmethod
    def talk(self):
        pass

    @abstractmethod
    def die(self):
        pass

    def show_atributes(self):
        print()
        print(f"\tName: {self.name}")
        print(f"\tAge: {self.age}")
        print(f"\tHealth: {self.health}")
        print(f"\tPlanethood: {self.planethood}")
        print(f"\tLanguague: {self.languague}")
        print()
