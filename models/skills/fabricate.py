from .skill import Skill

class Fabricate(Skill):
    def __init__(self, components:list):
        super().__init__("Fabricate")
        self.components = components

    def level_up(self):
        self.level += 1

    def use(self):
        pass