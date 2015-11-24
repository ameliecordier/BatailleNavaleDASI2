import ocean

#A déplacer plus tard dans une classe logique de jeu
def deciderDeJouer():
    print("Bienvenue dans ce jeu de Bataille Navale d'enfer !")
    reponse = input("Voulez-vous jouer avec moi ? (O / N) ")
    
    if reponse == "O":
        print("Youpi")
    elif reponse == "N":
        print("Tant pis")
    else:
        print("Je vous repose la question ?")
        reponse = deciderDeJouer()
    return reponse

#A déplacer plus tard... ? 
def demanderTailleOcean():
    X = input("Quel est la taille de X ? ")
    Y = input("Quel est la taille de Y ? ")
    print("Pour info, vous avez demandé un océan de " + X + "x" + Y)
    return int(X), int(Y)


#Programme principal
jouer = deciderDeJouer()

if jouer == "O":
    monoceanJ1bateaux = ocean()
    monoceanJ1tirs = ocean()
    monoceanJ2bateaux = ocean()
    monoceanJ2tirs = ocean()
    tailleX, tailleY = demanderTailleOcean()  
    monoceanJ1bateaux.construireOcean(tailleX, tailleY)
    monoceanJ1bateaux.construireOcean(tailleX, tailleY)
    monoceanJ2bateaux.construireOcean(tailleX, tailleY)
    monoceanJ2tirs.construireOcean(tailleX, tailleY)
    monoceanJ1bateaux.afficherOcean()


#TEST PAILLARES ^^
    



