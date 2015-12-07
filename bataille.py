#!/usr/bin/python
# -*- coding: utf-8 -*-

import ocean
import sys
#A déplacer plus tard dans une classe logique de jeu
def deciderDeJouer():
    print("Bienvenue dans ce jeu de Bataille Navale d'enfer !")
    reponse = input("Voulez-vous jouer avec moi ? (O / N) ")
    reponse = reponse.lower()

    if reponse == "o":
        print("Youpi")
    elif reponse == "n":
        print("Tant pis")
        sys.exit(0)
    else:
        print("Je vous repose la question ?")
        deciderDeJouer()


#A déplacer plus tard... ? 
def demanderTailleOcean():
    X = initialisationX()
    Y = initialisationY()
    print("Pour info, vous avez demandé un océan de " + str(X) + "x" + str(Y))
    return X, Y

def initialisationX():
    while True:
        try:
            x = int(input("La largeur sera de ? (10 à 26) : "))
            if 10<=x<=26:
                break
            else:
                print("Cet entier n'est pas compris entre 10 et 26")
        except ValueError:
              print("Ce n'est pas un entier!")

    return x


def initialisationY():
    while True:
        try:
            y = int(input("La hauteur sera de ? (10 à 26) : "))
            if 10<=y<=26:
                break
            else:
                print("Cet entier n'est pas compris entre 10 et 26")
        except ValueError:
              print("Ce n'est pas un entier!")

    return y


def afficherPlateau(oceanTirs, oceanBateaux, largeur, joueur):
    alphabet="   a b c d e f g h i j k l m n o p q r s t u v w x y z"
    print("PLATEAU DE JEU J"+joueur+":")
    print(alphabet[:largeur*2+2])
    oceanTirs.afficherOcean(1)
    separation = "  "
    for i in range(0, largeur*2+5):
        separation += "-"
    print(separation)
    print(alphabet[:largeur*2+2] + "  Bateaux")
    oceanBateaux.afficherOcean(2)
    print("")
    separation = ""
    for i in range(0, largeur+2):
        separation += "/\\"
    print(separation)

#Programme principal
deciderDeJouer()
monoceanJ1bateaux = ocean.ocean()
monoceanJ1tirs = ocean.ocean()
monoceanJ2bateaux = ocean.ocean()
monoceanJ2tirs = ocean.ocean()
tailleX, tailleY = demanderTailleOcean()
print('')

monoceanJ1bateaux.construireOcean(tailleX, tailleY)
monoceanJ1tirs.construireOcean(tailleX, tailleY)
monoceanJ2bateaux.construireOcean(tailleX, tailleY)
monoceanJ2tirs.construireOcean(tailleX, tailleY)

afficherPlateau(monoceanJ1tirs,monoceanJ1bateaux,tailleX, "1")

alphabet="abcdefghijklmnopqrstuvwxyz"
tirX = input("Saisissez la coordonnée X de votre tir (exemple : B): ")
tirX = tirX.lower()
while (tirX not in alphabet):
    print("Veuillez saisir une lettre")
    tirX = input("Saisissez la coordonnée X de votre tir (exemple : B): ")
    tirX = tirX.lower()
for i in range(0, len(alphabet)):
    if tirX == alphabet[i]:
        tirX = i+1
tirX = int(tirX)
tirY = int(input("Saisissez la coordonnée Y de votre tir (exemple : 15): "))
while tirY > 26 or tirY < 0:
    print("Erreur : veuillez saisir une valeur de 0 à 26")
    tirY = int(input("Saisissez la coordonnée Y de votre tir (exemple : 15): "))


