from .alive import Alive

class Martian(Alive):
    def __init__(self, name, age, health, planethood, inventory, skills, lang, intelligence):
        super().__init__(name, age, health, planethood, inventory, skills, lang, intelligence)