from ADF import *


def main():
    print("------------------")
    print("MODELISATEUR D'ADF")
    print("------------------\n")
    print("veuiller choisir votre mode d'entré des données")
    print("!!-> s <-!! saisie utilisateur  OU !!-> l <-!! pour lecture a partir d'un fichier .txt")

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
        copyAutomate = [newAutomate.etat.copy(), newAutomate.alphabet.copy(), newAutomate.Einit.copy(),
                        newAutomate.Efini.copy(), newAutomate.transition.copy()]
        options = ["A", "B", "C", "D"]
        conditionS = False
        choixS = ""
        while conditionS is not True:
            print("que souhaitez vous faire ? : \n" +
                  "A -> afficher les etats accessibles et coaccessibles\n" +
                  "B -> completer l'automate et affcher\n" +
                  "C -> determiner l'automate et afficher\n" +
                  "D -> juste afficher l'automate entré\n")
            conditionOptions = False
            choixOptions = ""
            while conditionOptions is not True:
                choixOptions = str(input("veuillez choisir entre A B C ou D : "))
                if choixOptions not in options:
                    conditionOptions = False
                else:
                    conditionOptions = True

            if choixOptions == "A":
                print("Que voulez vous ?\n" +
                      "1 -> liste des etats accesiible\n"
                      "2 -> liste des etas co-accessible\n")
                conditionAcces = False
                choixAcces = ""
                while conditionAcces is not True:
                    choixAcces = str(input("veuillez choisir entre 1 ou 2 : "))
                    if choixAcces not in ["1", "2"]:
                        conditionAcces = False
                    else:
                        conditionAcces = True
                if choixAcces == "1":
                    print(newAutomate.etats_accessibles())
                    if newAutomate.automate_accessible() is True:
                        print("cet automate est accessible")
                    else:
                        print("cet automate n'est pas accessible")
                else:
                    print(newAutomate.etats_coaccessibles())
                    if newAutomate.automate_coaccessible() is True:
                        print("cet automate est co-accessible")
                    else:
                        print("cet automate n'est pas co-accessible")
            elif choixOptions == "B":
                newAutomate.completer_automate()
                print("Voulez vous afficher l'automate ?")
                conditionAffichage = False
                choixAfichage = ""
                while conditionAffichage is not True:
                    choixAfichage = str(input("veuillez choisir entre oui 'o' ou non 'n' : "))
                    if choixAfichage not in ["o", "n"]:
                        conditionAffichage = False
                    else:
                        conditionAffichage = True
                if choixAfichage == "o":
                    nom_automate_complet = str(input("saisissez le nom de l'automate complet .gv(atttention à bien " +
                                                     "saisir!!) : "))
                    newAutomate.automate_img(nom_automate_complet)
                else:
                    print("OK")
            elif choixOptions == "C":
                newAutomate.determiniser_automate()
                conditionAffichage = False
                choixAfichage = ""
                while conditionAffichage is not True:
                    choixAfichage = str(input("veuillez choisir entre oui 'o' ou non 'n' : "))
                    if choixAfichage not in ["o", "n"]:
                        conditionAffichage = False
                    else:
                        conditionAffichage = True
                if choixAfichage == "o":
                    nom_automate_complet = str(input("saisissez le nom de l'automate complet .gv(atttention à bien " +
                                                     "saisir!!) : "))
                    newAutomate.automate_img(nom_automate_complet)
                else:
                    print("OK")

            elif choixOptions == "D":
                print("Voulez vous afficher l'automate ?")
                conditionAffichage = False
                choixAfichage = ""
                while conditionAffichage is not True:
                    choixAfichage = str(input("veuillez choisir entre oui 'o' ou non 'n' : "))
                    if choixAfichage not in ["o", "n"]:
                        conditionAffichage = False
                    else:
                        conditionAffichage = True
                if choixAfichage == "o":
                    nom_automate_complet = str(input("saisissez le nom de l'automate complet .gv(atttention à bien " +
                                                     "saisir!!) : "))
                    newAutomate.automate_img(nom_automate_complet)
                else:
                    print("OK")

            print("SOUHAITEZ VOUS CONTINUER LES OPERATIONS SUR L'AUTOMATE ?")
            lastcondition = False
            while lastcondition is not True:
                choixS = str(input("OUI 'o' ou NON 'n' : "))
                if choixS not in ["o", "n"]:
                    lastcondition = False
                else:
                    lastcondition = True
            if choixS == "o":
                conditionS = False
            else:
                conditionS = True
            newAutomate.etat = copyAutomate[0]
            newAutomate.alphabet = copyAutomate[1]
            newAutomate.Einit = copyAutomate[2]
            newAutomate.Efini = copyAutomate[3]
            newAutomate.transition = copyAutomate[4]

    else:
        nom_fichier = str(input("veuillez saisir le nom du fichier .txt (faire attention au chemin): "))
        info = compte_elements(nom_fichier)
        newAutomate = Automate(info[0], info[1], info[2], info[3])
        newAutomate.file_to_automate(nom_fichier)
        print("\n-------------------------\n")
        print(newAutomate.etat)
        print(newAutomate.alphabet)
        print(newAutomate.Einit)
        print(newAutomate.Efini)
        print("\n")
        print(newAutomate.transition)
        print("\n")
        copyAutomate = [newAutomate.etat.copy(), newAutomate.alphabet.copy(), newAutomate.Einit.copy(),
                        newAutomate.Efini.copy(), newAutomate.transition.copy()]
        options = ["A", "B", "C", "D"]
        conditionS = False
        choixS = ""
        while conditionS is not True:
            newAutomate.etat = copyAutomate[0]
            newAutomate.alphabet = copyAutomate[1]
            newAutomate.Einit = copyAutomate[2]
            newAutomate.Efini = copyAutomate[3]
            newAutomate.transition = copyAutomate[4]
            print("que souhaitez vous faire ? : \n" +
                  "A -> afficher les etats accessibles et coaccessibles\n" +
                  "B -> completer l'automate et affcher\n" +
                  "C -> determiner l'automate et afficher\n" +
                  "D -> juste afficher l'automate entré\n")
            conditionOptions = False
            choixOptions = ""
            while conditionOptions is not True:
                choixOptions = str(input("veuillez choisir entre A B C ou D : "))
                if choixOptions not in options:
                    conditionOptions = False
                else:
                    conditionOptions = True

            if choixOptions == "A":
                print("Que voulez vous ?\n" +
                      "1 -> liste des etats accesiible\n"
                      "2 -> liste des etas co-accessible\n")
                conditionAcces = False
                choixAcces = ""
                while conditionAcces is not True:
                    choixAcces = str(input("veuillez choisir entre 1 ou 2 : "))
                    if choixAcces not in ["1", "2"]:
                        conditionAcces = False
                    else:
                        conditionAcces = True
                if choixAcces == "1":
                    print(newAutomate.etats_accessibles())
                    if newAutomate.automate_accessible() is True:
                        print("cet automate est accessible")
                    else:
                        print("cet automate n'est pas accessible")
                else:
                    print(newAutomate.etats_coaccessibles())
                    if newAutomate.automate_coaccessible() is True:
                        print("cet automate est co-accessible")
                    else:
                        print("cet automate n'est pas co-accessible")
            elif choixOptions == "B":
                newAutomate.completer_automate()
                print("Voulez vous afficher l'automate ?")
                conditionAffichage = False
                choixAfichage = ""
                while conditionAffichage is not True:
                    choixAfichage = str(input("veuillez choisir entre oui 'o' ou non 'n' : "))
                    if choixAfichage not in ["o", "n"]:
                        conditionAffichage = False
                    else:
                        conditionAffichage = True
                if choixAfichage == "o":
                    nom_automate_complet = str(input("saisissez le nom de l'automate complet .gv(atttention à bien " +
                                                     "saisir!!) : "))
                    newAutomate.automate_img(nom_automate_complet)
                else:
                    print("OK")
            elif choixOptions == "C":
                newAutomate.determiniser_automate()
                conditionAffichage = False
                choixAfichage = ""
                while conditionAffichage is not True:
                    choixAfichage = str(input("veuillez choisir entre oui 'o' ou non 'n' : "))
                    if choixAfichage not in ["o", "n"]:
                        conditionAffichage = False
                    else:
                        conditionAffichage = True
                if choixAfichage == "o":
                    nom_automate_complet = str(input("saisissez le nom de l'automate complet .gv(atttention à bien " +
                                                     "saisir!!) : "))
                    newAutomate.automate_img(nom_automate_complet)
                else:
                    print("OK")

            elif choixOptions == "D":
                print("Voulez vous afficher l'automate ?")
                conditionAffichage = False
                choixAfichage = ""
                while conditionAffichage is not True:
                    choixAfichage = str(input("veuillez choisir entre oui 'o' ou non 'n' : "))
                    if choixAfichage not in ["o", "n"]:
                        conditionAffichage = False
                    else:
                        conditionAffichage = True
                if choixAfichage == "o":
                    nom_automate_complet = str(input("saisissez le nom de l'automate complet .gv(atttention à bien " +
                                                     "saisir!!) : "))
                    newAutomate.automate_img(nom_automate_complet)
                else:
                    print("OK")

            print("SOUHAITEZ VOUS CONTINUER LES OPERATIONS SUR L'AUTOMATE ?")
            lastcondition = False
            while lastcondition is not True:
                choixS = str(input("OUI 'o' ou NON 'n' : "))
                if choixS not in ["o", "n"]:
                    lastcondition = False
                else:
                    lastcondition = True
            if choixS == "o":
                conditionS = False
            else:
                conditionS = True



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
