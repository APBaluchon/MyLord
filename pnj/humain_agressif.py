from pnj.humain import Humain

class HumainAgressif(Humain):

    def __init__(self, nom="", hp=10, action=None, objet=None, profession="", attack=5):
        super().__init__(nom, hp, action, objet, profession)
        self.attack = 5