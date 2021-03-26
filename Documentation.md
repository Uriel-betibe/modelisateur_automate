# modelisateur_automate

insaller le module graphviz avant de lancer le programme :)

format des fichier.txt en lecture:

 - L0 Etats de l'automate (sépareateur : ";")
 - L1 Alphabet (sépareateur : ";")
 - L2 Etats Initiaux (sépareateur : ";")
 - L3 Etats finaux (sépareateur : ";")
 - L4 à LN Transitions(Etat;symbot;etat_arrivé) (sépareateur : ";")

infos sur les foncions :

//ADF.py
def compte_elements(nom_fichier)
   @param str<nom_fichier.txt>
   elle recupere les nombre d'éléments de l'automate
   return list [nbEtat, nbSymbol, nbEinit, nbEfini]

def ecriture(fichier, instance)
  @param str<fichier.txt>
  @param instance parmis (Etat;symbot;etat_init,etat_fini)
  ecris dans le fichier l'instance

def ecriture_transition(fichier, instance)
  @param str<fichier.txt>
  @param instance (transition)
  ecris dans le fichier l'instance

def supprimerDoublons(liste):
    @param type list
    suprime les doublons présent dasn une liste

Class:
    Automate
        @:parameter nbEtat : difinit le nombre d'état de notre ensemble
        @:parameter tAlphabet: definit la longuer de notre alphabet
        @:parameter nbEinit: nombre d'états initiaux
        @:parameter nbEfini: nombre d'états finaux
        la class Automate permet de représenter un automate et grace aux methodes de la class
        lu appliquer les opérations aplicable aux automates

    methods :

    def set_Etat(self)
        set tous l'ensemble des etats en mode saisie lors de l'execution
        @param self

    def set_Alphabet(self)
        set l'alphabet en mode saisie lors de l'execution
        @param self

    def set_Etat_init(self)
        set les etats initiaux en mode saisie lors de l'execution
        @param self

    def set_Etat_fini(self)
        set les etats finaux en mode saisie lors de l'execution
        @param self

    def set_Transiton(self)
        set les transtions des etats  en mode saisie lors de l'execution
        @param self

    def automate_to_file(self, nom_fichier)
        converti les informations de l'automate en un fichier .txt
        @param self
        @param nom_fichier <str> nom du fichier de destination

    def file_to_automate(self, nom_fichier)
        converti les informations d'un fichier.txt respectant les normes etablis vers un automate traitable
        @param self
        @param nom_fichier <str> nom du fichier de lecture

    def automate_img(self, nom_model)
        modelise les informations de l'automate et renvoie une image de l'automate
        @param self
        @param nom_model <str> nom du fichier de lecture

    def successeur(self, etat)
        renvoie une liste des etats suivant  d'un etat donné
        @param self
        @param etat
        @return list des successeurs de l'etat

    def predecesseur(self, etat)
        renvoie une liste des etats precedant  d'un etat donné
        @param self
        @param etat
        @return list des predecesseurs de l'etat

    def is_complete(self)
        verifie si un etat est deja COMPLET
        @param self
        @return bool

    def completer_automate(self)
        complete un automate si ce dernier n'est pas deja complet
        @param self


    def etats_accessibles(self)
        renvoie une list de tous les etas accessibles de l'automate
        @param self
        @return list d'etats accessibles

    def est_accessible(self, etat)
        renvoie True si l'etat est accessible dans l'automate
        @param self
        @param etat
        @return bool

    def automate_accessible(self)
        renvoie True si l'automate est accessible dans dans le cas ou tous les etats sont accessible
        @param self
        @return bool

    def etats_coaccessibles(self)
        renvoie une list de tous les etas co-accessibles de l'automate
        @param self
        @return list d'etats accessibles

    def est_coaccessible(self, etat)
        renvoie True si l'etat est co-accessible dans l'automate
        @param self
        @param etat
        @return bool

    def automate_coaccessible(self)
        renvoie True si l'automate est co-accessible dans dans le cas ou tous les etats sont co-accessible
        @param self
        @return bool

    def determiniser_automate(self)
        Determinise l'automate dans le cas ou ce drnier ne l'est pas deja
        @self
        @return self

//main.py

def main()
    fonction d'exécution
    @param none
    @return none