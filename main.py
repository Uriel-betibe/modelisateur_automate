from ADF import Automate


def main():
    newAutomate = Automate(3,2,1,1)
    newAutomate.set_Etat()
    newAutomate.set_Alphabet()
    newAutomate.set_Etat_init()
    newAutomate.set_Etat_fini()
    newAutomate.set_Transiton()
    print("-------------------------")
    print(newAutomate.etat)
    print(newAutomate.alphabet)
    print(newAutomate.Einit)
    print(newAutomate.Efini)
    print("\n \n")
    print(newAutomate.transition)
    # creation de fichier
    newAutomate.automate_to_file("test.txt")

main()
