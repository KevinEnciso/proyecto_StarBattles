from .character import Character

class Robot(Character):
    def __init__(self, name, age, health, planethood, inventory, skills, lang, ia):
        super().__init__(name, age, health, planethood, inventory, skills, lang)
        self.ia = ia
        self.signal = 10
    
    def sync():
        pass