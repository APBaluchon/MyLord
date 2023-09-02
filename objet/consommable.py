from objet.objet import Objet

class Consommable(Objet):

    def __init__(self, nom=None, prix=0, description=None, action=None):
        super().__init__(nom, prix, description)
        self.action = action