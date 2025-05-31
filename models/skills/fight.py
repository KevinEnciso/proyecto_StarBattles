from .skill import Skill

class Fight(Skill):
    def __init__(self, weapon, target_character):
        super().__init__("Fight")
        self.weapon = weapon
        self.objetive_character = target_character

    def level_up(self):
        self.level += 1

    def use(self):
        pass