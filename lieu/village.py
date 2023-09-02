from lieu.lieu import Lieu

class Village(Lieu):

    def __init__(self, nom="", pnj=None, action=None):
        super().__init__(nom, pnj, action)