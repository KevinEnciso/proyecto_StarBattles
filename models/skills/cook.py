from .skill import Skill

class Cook(Skill):
    def __init__(self, food:list):
        super().__init__("Cook")
        self.food = food

    def use(self):
        pass