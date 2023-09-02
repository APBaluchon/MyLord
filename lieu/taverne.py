from lieu.lieu import Lieu

class Taverne(Lieu):

    def __init__(self):
        super().__init__("Taverne",
                         None,
                         ["1 - Aller au village"],
                          ",^,\n")
        
    def agir(self, choix, game):
        if(choix == "1"):
            game.changerLieu("Village")
