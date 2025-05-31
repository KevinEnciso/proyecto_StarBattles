from models.objects.object import Object

class Inventory:
    def __init__(self, items:list, size:int, using:Object):
        self.items = items
        self.size = size
        self.using = using
    
    def expand(self):
        pass

    def show_items(self):
        print(self.items)