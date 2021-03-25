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
from graphviz import Digraph
import re



def ecriture(fichier, instance):
    for i in range(len(instance)):
        fichier.write(instance[i])
        if i < len(instance)-1:
            fichier.write(";")
    fichier.write("\n")


def ecriture_transition(fichier, instance):
    for transition in instance:
        x = transition[0] + ";" + transition[1] + ";" + transition[2]
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
        self.transition = []

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
        ajoutTransition = True
        while ajoutTransition:
            ajoutOK = False
            while ajoutOK is not True:
                etatDepart = str(input("saisissez l'état de depart de la transiion: "))
                alphaTransition = str(input("saisissez le symbole de cette transition: "))
                etatArrive = str(input("saisissez l'état d'arrivé de cette transision: "))
                if (etatDepart in self.etat) and (alphaTransition in self.alphabet) and (etatArrive in self.etat):
                    self.transition.append([etatDepart,alphaTransition,etatArrive])
                    ajoutOK = True
                else:
                    print("mauvaise saisie assurez vous de respecté l'ensemble des etats et l'alphabet")
            continuer = str(input("souhaitez ajouter une autre transition 'o' (oui) ou 'n' (non): "))
            if continuer == "n":
                ajoutTransition = False
            
        """ 
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
        """

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
        liste = fichier.readlines()
        for i in range(len(liste)):
            liste[i] = re.sub('[\n]', '', liste[i])
        #enregistrement des etats
        lesEtats = liste[0].split(";")
        self.etat = lesEtats
        # enregistrement de l'alphabet
        language = liste[1].split(";")
        self.alphabet = language
        # enregistrement etat initial
        if len(liste[2]) > 1:
            EtatInitial = liste[2].split(";")
            self.Einit = EtatInitial
        else:
            self.Einit = [liste[2]]
        # enregistrement etat final
        if len(liste[3]) > 1:
            EtatFinal = liste[3].split(";")
            self.Efini = EtatFinal
        else:
            self.Efini = [liste[3]]
        # enregistrement transition
        for i in range(4, len(liste)):
            transitionTeta = liste[i].split(";")
            self.transition.append(transitionTeta)
        fichier.close()

    def automate_img(self,nom_model):
        D = Digraph('automate', filename=nom_model)
        for transiton in self.transition:
            D.edge(transiton[0], transiton[2], transiton[1])
        D.view()
        #todo ajouter un signe pour la représentation de l'état initial et l'etat final

    # todo developper la fonction de derterminisation de l'automate
    def determiniser_automate(self):
        deterministe = True
        if len(self.Einit) > 1:
            deterministe = False
        pass
    
