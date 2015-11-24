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
    monocean = ocean()
    tailleX, tailleY = demanderTailleOcean()  
    monocean.construireOcean(tailleX, tailleY)
    monocean.afficherOcean()

    



