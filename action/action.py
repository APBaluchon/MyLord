from abc import ABC, abstractmethod

class Action(ABC):
    def __init__(self, nom=None, cible=None):
        self.nom = nom
        self.cible = cible

    @abstractmethod
    def agir(self):
        pass