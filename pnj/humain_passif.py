from pnj.humain import Humain

class HumainPassif(Humain):

    def __init__(self, nom="", hp=10, action=None, objet=None, profession=""):
        super().__init__(nom, hp, action, objet, profession)