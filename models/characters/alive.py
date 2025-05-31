from .character import Character
from abc import abstractmethod

class Alive(Character):
    def __init__(self, name, age, health, planethood, inventory, skills, lang, intelligence):
        super().__init__(name, age, health, planethood, inventory, skills, lang)
        self.hunger = 0
        self.sanity = 100
        self.intelligence = intelligence

    @abstractmethod
    def eat():
        pass
    