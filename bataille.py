# -*- coding: utf8 -*-

import os ##Pour nétoyer l'écran
import demandeTailleOcean
import classeOcean
import typeBateau
import classeBateau
        
##Fonction demandeDebutPartie
##Demande à l'utilisateur s'il veut commencer une partie
##Renvoie "o" ou "n" (maj ou min)
def demandeDebutPartie():
    rep = input("Voulez-vous jouer ? (o/n) : ")
    
    if not (rep == "o" or rep == "n" or rep == "O" or rep == "N"):
        print("Vous ne pouvez répondre que oui ou non !")
        rep = demandeDebutPartie()
    elif rep == "O":
        rep = "o"
    elif rep == "N":
        rep = "n"

    return rep



##Fonction demandeNbBateau
##Retourne le nombre de bateaux de chaque type que les joueurs auront (rentrer au clavier)
def demandeNbBateau(arsenal):
    for i in range(0, len(arsenal.nomBateau)):
        err = 1        
        while err == 1:
            arsenal.nbBateau[i] = input("Nombre de " + arsenal.nomBateau[i] + " (taille " + str(arsenal.tailleBateau[i]) + ") ? ")
            
            try:
                arsenal.nbBateau[i] = int(arsenal.nbBateau[i])
                assert arsenal.nbBateau[i] > 0               
                err = 0
            except ValueError:
                print("Veuillez rentrer un entier !")
            except AssertionError:
                print("Un nombre est forcement positif !")



##
def demandeJeu(arsenal):
    while True:
        jeu = input("Quel set de bateaux voulez-vous ? (Défaut (d) / Perso (p)) : ")

        if jeu == 'd':
            break
        elif jeu == 'p':
            demandeNbBateau(arsenal)
            break
##        else:
##            print("Erreur")



##Fonction main
##Déroule une partie
##Retourne 1 s'il y a eu une partie de joué, 0 sinon
def main():   
    rep = demandeDebutPartie()

    if rep != "o":
        return 0
    else:
        x, y = demandeTailleOcean.demandeTailleOcean()
        
        oceanJoueur1 = classeOcean.ocean(x, y)
        oceanJoueur2 = classeOcean.ocean(x, y)
        oceanBateauJoueur1 = classeOcean.ocean(x, y)
        oceanBateauJoueur2 = classeOcean.ocean(x, y)

        arsenal = typeBateau.arsenal()
        demandeJeu(arsenal)
        
        os.system("cls")         
        print("Joueur 1, virez le joueur 2 et placez vos bateaux.")
        classeBateau.construitListeBateaux(arsenal, oceanBateauJoueur1)
        print("Bravo, vous avez placé tous vos bateaux.")
        
        os.system("cls")
        print("\nJoueur 2, virez le joueur 1 et placez vos bateaux.\n")
        classeBateau.construitListeBateaux(arsenal, oceanBateauJoueur2)
        print("Bravo, vous avez placé tous vos bateaux.")
        
        os.system("cls")
        print("Début de la partie")
        ## a finir
        
        return 1



##Début de l'execution
os.system('cls') 
print("Bonjour et bienvenue...")

##Tant que des parties sont jouées, on relance des parties.
while main() == 1:
    os.system("cls")  
    
print("Au revoir et merci d'avoir joué !")
