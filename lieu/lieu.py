from abc import ABC, abstractmethod

class Lieu(ABC):
    def __init__(self, nom= "", pnj= None, action= None):
        self.nom = nom
        self.pnj = pnj
        self.action = action