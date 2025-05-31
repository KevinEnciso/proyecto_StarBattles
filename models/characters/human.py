from .alive import Alive

class Human(Alive):
    def __init__(self, name, age, health, planethood, inventory, skills, lang, intelligence):
        super().__init__(name, age, health, planethood, inventory, skills, lang, intelligence)