from objet.objet import Objet

class Ressource(Objet):
    def __init__(self, nom=None, prix=0, description=None):
        super().__init__(nom, prix, description)