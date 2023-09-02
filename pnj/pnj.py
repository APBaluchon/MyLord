from abc import ABC, abstractmethod

class Pnj(ABC):
    def __init__(self, nom="", hp=10, action=None, objet=None):
        self.nom = nom
        self.hp = hp
        self.action = action
        self.object = objet