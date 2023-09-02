from abc import ABC, abstractmethod

class Lieu(ABC):
    def __init__(self, nom= "", pnj= None, action= None, visuel=None):
        self.nom = nom
        self.pnj = pnj
        self.action = action
        self.visuel = visuel

    @abstractmethod
    def agir(self, choix, game):
        pass
