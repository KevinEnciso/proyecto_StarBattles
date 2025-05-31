from models.objects.items.item import Item

class Food(Item):
    def __init__(self, name:str, durability:int, cost:int, fill:int):
        super().__init__(name, durability, cost)
        self.fill = fill
    
    def use(self):
        pass