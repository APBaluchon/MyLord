from abc import ABC, abstractmethod
from pnj.pnj import Pnj

class Humain(Pnj, ABC):

    def __init__(self, nom="", hp=10, action=None, objet=None, profession=""):
        super().__init__(nom, hp, action, objet)
        self.profession = profession