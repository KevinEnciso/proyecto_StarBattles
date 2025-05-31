from abc import ABC, abstractmethod

class Skill(ABC):
    def __init__(self, name: str):
        self.name = name
        self.level = 0
    
    @abstractmethod
    def use(self):
        pass