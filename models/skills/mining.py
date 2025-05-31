from .skill import Skill
from models.objects.items.ore import Ore

class Mining(Skill):
    def __init__(self, target_ore: Ore):
        super().__init__("Mining", 0)
        self.target_ore = target_ore
    
    def use():
        pass