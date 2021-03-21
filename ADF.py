"""
@Author : Uriel SAMBIANI
@Description : programme de modelisation d'un automate à partir de :
    - saisies utilisation
    - lecture d'un fichier .txt
Le programme est capable :
    - d'afficher l'automate à l'écran
    - d'afficher / lister les états accessibles et co-accessibles
    - de compléter l'automate
    - de déterminiser l'automate en détaillant les étapes

"""

class Automate:
    """
    @:parameter nbEtat : difinit le nombre d'état de notre ensemble
    @:parameter tAlphabet: definit la longuer de notre alphabet
    @:parameter nbEinit: nombre d'états initiaux
    @:parameter nbEfini: nombre d'états finaux
    """
    def __init__(self, nbEtat, tAlphabet, nbEinit, nbEfini):
        self.nombreEtat = nbEtat
        self.tailleAlphabet = tAlphabet
        self.nombreEtatInit = nbEinit
        self.nombreEtatFini = nbEfini
        self.etat = []
        self.alphabet = []
        self.Einit = []
        self.Efini = []
        self.transition = {}

    def set_Etat(self):
        for i in range(self.nombreEtat):
            temp = str(input("veuillez saisir l'état : "))
            self.etat.append(temp)
        print("saisie de états reussi :")
        print(self.etat)


    def set_Alphabet(self):
        pass

    def set_Etat_init(self):
        pass

    def set_Etat_fini(self):
        pass

    def set_Transiton(self):
        pass
