from abc import ABC, abstractmethod

class Objet(ABC):

    def __init__(self, nom=None, prix=0, description=None):
        self.nom = nom
        self.prix = prix
        self.description = description