from ADF import Automate


def main():
    print("------------------")
    print("MODELISATEUR D'ADF")
    print("------------------\n")
    print("veuiller choisir votre mode d'entré des données")
    print("saisie utilisateur (s) lecture a partir d'un fichier .txt (l)")

    # todo developper une fonction qui renvoi les nombres d'éléments dans un fichier
    conditionChoix = False
    choix = ""
    while conditionChoix is not True:
        choix = str(input("saisir (s) ou lire (l) : "))
        if (choix == 's') or (choix == 'l'):
            conditionChoix = True
        else:
            conditionChoix = False

    if choix == 's':
        print("----------")
        print("MODE SAISI: \n")
        print("----------")
        nbE = int(input("veuillez sasir le nombre d'etats :"))
        nbS = int(input("veuillez sasir le nombre de symboles de l'alphabet :"))
        nbEI = int(input("veuillez sasir le nombre d'etat initial :"))
        nbEF = int(input("veuillez sasir le nombre d'etat Final :"))
        newAutomate = Automate(nbE, nbS, nbEI, nbEF)
        newAutomate.set_Etat()
        newAutomate.set_Alphabet()
        newAutomate.set_Etat_init()
        newAutomate.set_Etat_fini()
        newAutomate.set_Transiton()
        print("\n-------------------------\n")
        print(newAutomate.etat)
        print(newAutomate.alphabet)
        print(newAutomate.Einit)
        print(newAutomate.Efini)
        print("\n")
        print(newAutomate.transition)

    else:
        nbE = int(input("veuillez sasir le nombre d'etats :"))
        nbS = int(input("veuillez sasir le nombre de symboles de l'alphabet :"))
        nbEI = int(input("veuillez sasir le nombre d'etat initial :"))
        nbEF = int(input("veuillez sasir le nombre d'etat Final :"))
        newAutomate = Automate(nbE, nbS, nbEI, nbEF)
        nom_fichier = str(input("veuillez saisir le nom du fichier .txt (faire attention au chemin): "))
        newAutomate.file_to_automate(nom_fichier)
        print("\n-------------------------\n")
        print(newAutomate.etat)
        print(newAutomate.alphabet)
        print(newAutomate.Einit)
        print(newAutomate.Efini)
        print("\n")
        print(newAutomate.transition)
        print("\n")
        # todo option de choix a l'utilisateur de voir si l'automate est determiniser
        newAutomate.determiniser_automate()
        print("\n-------------------------\n")
        print(newAutomate.etat)
        print(newAutomate.alphabet)
        print(newAutomate.Einit)
        print(newAutomate.Efini)
        print("\n")
        # newAutomate.supprimerDoublons()
        print(newAutomate.transition)
        print("\n")

    # creation de fichier
    conditionChoix2 = False
    choix2 = ''
    while conditionChoix2 is not True:
        choix2 = str(input("souhaitez vous enregistrer l'automate dans un fichier de lecture o/n : "))
        if (choix2 == 'o') or (choix2 == 'n'):
            conditionChoix2 = True
        else:
            conditionChoix2 = False

    if choix2 == 'o':
        nom_fichier_enregistre = str(input("veuillez saisir le nom du fichier .txt : "))
        newAutomate.automate_to_file(nom_fichier_enregistre)
    # creation de l'image du
    nom_modele = str(input("veuillez saisir le nom du fichier .gv pour la représentation de l'automate: "))
    newAutomate.automate_img(nom_modele)


main()
