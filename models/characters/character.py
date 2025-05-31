from abc import ABC, abstractmethod
from inventory import Inventory
from models.objects.components.planet import Planet

class Character(ABC):
    def __init__(self, name: str, age: int, health: int, planethood: Planet, inventory: Inventory, skills, lang: str):
        self.name = name
        self.age = age
        self.health = health
        self.planethood = planethood
        self.inventoty = inventory
        self.skills = skills
        self.lang = lang

    @abstractmethod
    def talk(self):
        pass

    @abstractmethod
    def die(self):
        pass

    def show_atributes(self):
        print(self.name)
        print(f"\tAge: {self.age}")
        print(f"\tHealth: {self.health}")
        print(f"\planethood: {self.planethood}")
        print(f"\tLanguaje: {self.lang}")
