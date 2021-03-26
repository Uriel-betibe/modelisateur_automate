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


def supprimerDoublons(liste):
    for element in liste:
        if liste.count(element) >= 2:
            liste.remove(element)


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
                    self.transition.append([etatDepart, alphaTransition, etatArrive])
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
        ecriture(fichier, self.etat)
        # ecriture de l'alphabet
        ecriture(fichier, self.alphabet)
        # ecriture etat initial/aux
        ecriture(fichier, self.Einit)
        # ecriture etat final
        ecriture(fichier, self.Efini)
        # ecriture transition teta
        ecriture_transition(fichier, self.transition)
        fichier.close()

    def file_to_automate(self, nom_fichier):
        fichier = open(nom_fichier, 'r')
        liste = fichier.readlines()
        for i in range(len(liste)):
            liste[i] = re.sub('[\n]', '', liste[i])
        # enregistrement des etats
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

    def automate_img(self, nom_model):
        D = Digraph('automate', filename=nom_model)
        for transiton in self.transition:
            if transiton[0] in self.Einit:
                D.node(transiton[0], label=transiton[0], color="red")
            elif transiton[0] in self.Efini:
                D.node(transiton[0], label=transiton[0], shape="doublecircle")
            else:
                D.node(transiton[0], label=transiton[0])
            if transiton[2] in self.Einit:
                D.node(transiton[2], label=transiton[2], shape="doublecircle")

            D.edge(transiton[0], transiton[2], transiton[1])
        D.view()

    def successeur(self, etat):
        if etat not in self.etat:
            print("cet etat :"+etat+" ne fait pas parti de l'ensemble Q de cet automate")
            return
        succesor = []
        for transitionQ in self.transition:
            if transitionQ[0] == etat:
                if etat not in succesor:
                    succesor.append(transitionQ[2])
        return succesor

    def predecesseur(self, etat):
        if etat not in self.etat:
            print("cet etat :" + etat + " ne fait pas parti de l'ensemble Q de cet automate")
            return
        predecessor = []
        for transitionQ in self.transition:
            if transitionQ[2] == etat:
                if etat not in predecessor:
                    predecessor.append(transitionQ[0])

    def is_complete(self):
        for etat in self.etat:
            i = 0
            for symbol in self.alphabet:
                for transitionA in self.transition:
                    if transitionA[:2] == [etat, symbol]:
                        i += 1
            if i < len(self.alphabet):
                return False
        return True

    def completer_automate(self):
        if self.is_complete() is True:
            return
        # on rejoute l'état poubelle a l'ensemble des etats
        EtatPoubel = "Qp"
        self.etat.append(EtatPoubel)
        EtatxSymbol = [element[:2] for element in self.transition]
        for etat in self.etat:
            for symbol in self.alphabet:
                if [etat,symbol] not in EtatxSymbol:
                    self.transition.append([etat, symbol, EtatPoubel])

    def determiniser_automate(self):
        deterministe = True
        casAtraiter = []
        casTraiter = []
        copyTransison = self.transition.copy()

        for transitionP in copyTransison:
            copy = copyTransison
            print("------ statut des transitions lors de la copy -------")
            print(self.transition)
            print("----------")
            copy.remove(transitionP)
            for transition in copy:
                if transitionP[:2] == transition[:2]:
                    if transitionP not in casAtraiter:
                        casAtraiter.append(transitionP)
                        casAtraiter.append(transition)

        if (len(casAtraiter) > 0) or (len(self.Einit) > 1):
            deterministe = False

        if deterministe is False:
            # creer un nouvel état initial qui combine tous les etats initaux
            if len(self.Einit) > 1:
                newEtatInitial = ""
                for i in range(len(self.Einit)):
                    newEtatInitial += self.Einit[i]
                    if i < len(self.Einit) - 1:
                        newEtatInitial += ","
                self.etat.append(newEtatInitial)
                # self.Einit = [newEtatInitial]
                # for transitionD in self.transition:
                # if (transitionD[0] in newEtatInitial) and (transitionD[2] in newEtatInitial):
                #   transitionD[0] = newEtatInitial

                for transitionD in self.transition:
                    if transitionD[0] in self.Einit[0]:
                        transitionD[0] = newEtatInitial
                self.Einit = [newEtatInitial]

            # gerer les transition et nouvelles transitions
            if len(casAtraiter) > 0:
                for teta in casAtraiter:
                    if teta not in casTraiter:
                        for delta in casAtraiter:
                            if delta is not teta:
                                if teta[:2] == delta[:2]:
                                    newEtat = "{},{}".format(teta[2], delta[2])
                                    print("------ new etat  -------")
                                    print(newEtat)
                                    print("----------")
                                    newtransition = [teta[0], teta[1], newEtat]
                                    for i in range(len(self.transition)):
                                        print("------ statut des transitions -------")
                                        print(self.transition)
                                        print("----------")
                                        if self.transition[i][:2] == newtransition[:2]:
                                            self.transition[i] = newtransition
                                            for transitionD in self.transition:
                                                if transitionD[0] in newEtat:
                                                    transitionD[0] = newEtat
                                    casTraiter.append(teta)
                                    casTraiter.append(delta)
                                    self.etat.append(newEtat)
                                    supprimerDoublons(self.transition)

            if deterministe is True:
                return
            elif deterministe is False:
                self.determiniser_automate()

    # todo fonction d' accessibilité et de co accessibilité
    def accessibilite(self):
        pass

    def coaccessibilite(self):
        pass