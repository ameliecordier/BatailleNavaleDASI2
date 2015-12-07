# -*- coding: utf8 -*-

##Fonction demandeTailleOcean
##Demande à l'utilisateur la longueur et la largeur de l'océean à créer
##Renvoie deux entiers positifs
def demandeTailleOcean():
    print("Quelle taille d'océan voulez-vous ?")
    
    err = 1    
    while err == 1:
        x = input("Longueur (entre 10 et 26) : ")
    
        try:
            x = int(x)
            assert ((x >= 10) and (x <= 26))
            err = 0
        except ValueError:
            print("Veuillez rentrer un entier !")
        except AssertionError:
            print("La longueur doit être comprise entre 10 et 26 !")
            
    err = 1    
    while err == 1:
        y = input("Hauteur (entre 10 et 26) : ")
    
        try:
            y = int(y)
            assert ((y >= 10) and (y <= 26))
            err = 0
        except ValueError:
            print("Veuillez rentrer un entier !")
        except AssertionError:
            print("La Hauteur doit être comprise entre 10 et 26 !")
    
    return x, y
