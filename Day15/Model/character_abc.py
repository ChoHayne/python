from abc import ABC, abstractmethod

class Characters(ABC):
    def __init__(self,name, health):
        self.name = name
        self.health = health

    @abstractmethod
    def attack(self):
        pass
    @abstractmethod
    def defend(self):
        pass
    @abstractmethod
    def special(self):
        pass