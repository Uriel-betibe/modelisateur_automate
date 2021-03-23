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


def ecriture(fichier, instance):
    for i in range(len(instance)):
        fichier.write(instance[i])
        if i < len(instance)-1:
            fichier.write(";")
    fichier.write("\n")


def ecriture_transition(fichier, instance):
    for key in instance:
        x = str(key) + ":" + str(instance[key])
        fichier.write(x+"\n")


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
            temp = str(input("veuillez saisir l'état " + str(i)+" :"))
            self.etat.append(temp)
        print("saisie de états reussi :")
        print(self.etat)


    def set_Alphabet(self):
        for i in range(self.tailleAlphabet):
            temp = str(input("veuillez saisir les symboles de l'alphabet : "))
            self.alphabet.append(temp)
        print("saisie de l'alphabet reussi :")
        print(self.alphabet)


    def set_Etat_init(self):
        for i in range(self.nombreEtatInit):
            conditionEI = False
            while conditionEI is not True:
                temp = str(input("veuillez saisir l'état de depart : "))
                if temp not in self.etat:
                    print("erreur! Votre saisie n'appartient a l'ensmble Q :")
                    print(self.etat)
                else:
                    self.Einit.append(temp)
                    conditionEI = True
        print("saisie Réussie voici le/les q0 : ")
        print(self.Einit)


    def set_Etat_fini(self):
        for i in range(self.nombreEtatFini):
            conditionEF = False
            while conditionEF is not True:
                temp = str(input("veuillez saisir l'état final : "))
                if temp not in self.etat:
                    print("erreur! Votre saisie n'appartient a l'ensmble Q :")
                    print(self.etat)
                else:
                    self.Efini.append(temp)
                    conditionEF = True
        print("saisie Réussie voici le/les F : ")
        print(self.Efini)


    def set_Transiton(self):
        print("Veuiller definir les transisiton :")
        for etat in self.etat:
            for lettre in self.alphabet:
                teta = (etat, lettre)
                print(teta)
                conditionT = False
                while conditionT is not True:
                    etatTransi = str(input("veuillez saisir q' si il existe, si non pressé entré : "))
                    if (etatTransi in self.etat) or (etatTransi == ""):
                        self.transition.update({teta: etatTransi})
                        conditionT = True
                    else:
                        print("erreur! Votre saisie n'appartient a l'alphabet ou n'est pas null :")
                        print(self.alphabet)

    def automate_to_file(self, nom_fichier):
        fichier = open(nom_fichier, 'w')
        # ecriture des etats :
        ecriture(fichier,self.etat)
        # ecriture de l'alphabet
        ecriture(fichier,self.alphabet)
        # ecriture etat initial/aux
        ecriture(fichier,self.Einit)
        # ecriture etat final
        ecriture(fichier,self.Efini)
        # ecriture transition teta
        ecriture_transition(fichier,self.transition)
        fichier.close()

    def file_to_automate(self,nom_fichier):
        fichier = open(nom_fichier, 'r')

        fichier.close()
        pass

    def automate_img(self):
        pass

