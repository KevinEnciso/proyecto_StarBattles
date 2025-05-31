from .skill import Skill

class Social(Skill):
    def __init__(self, target_character=None):
        super().__init__("Social")
        self.target_character = target_character
    
    def level_up(self):
        self.level += 1

    def use(self):
        pass