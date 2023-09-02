from lieu.lieu import Lieu

class Village(Lieu):

    def __init__(self):
        super().__init__("Village",
                         None,
                         ["1 - Aller à la taverne"],
                          ",^,\n")
        
    def agir(self, choix, game):
        if(choix == "1"):
            game.changerLieu("Taverne")
