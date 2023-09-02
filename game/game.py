from joueur.joueur import Joueur
from lieu.village import Village
from lieu.taverne import Taverne
import os

class Game:
    def __init__(self):
        pass

    def run(self):
        # tester si un fichier de sauvegarde existe déjà, si oui, le charger, sinon, le créer
        self.creationJoueur()
        self.creationLieu()
        self.boucle()

    def creationJoueur(self):
        myPlayer = Joueur("Marcel", 150, 2, None)
        self.myPlayer = myPlayer

    def creationLieu(self):
        self.lieu = [Village(), Taverne()]
        self.lieuActuel = self.lieu[0]

    def trouverLieu(self, nom):
        for i in range(len(self.lieu)):
            if(self.lieu[i].nom == nom):
                return i

    def changerLieu(self, nom):
        self.lieuActuel = self.lieu[self.trouverLieu(nom)]

    def boucle(self):
        while(True):
            os.system("cls")
            print(self.lieuActuel.nom)
            print("-"*50)
            print(self.lieuActuel.visuel)
            print("\n".join(self.lieuActuel.action))
            print("-"*50)
            choix = input("Choix :")
            self.lieuActuel.agir(choix, self)
            self.sauvegarder()

    def sauvegarder(self):
        pass


    