from models.objects.items.item import Item

class Weapon(Item):
    def __init__(self, name:str, durability:int, cost:int, damage:int):
        super().__init__(name, durability, cost)
        self.damage = damage
    
    def use(self):
        pass