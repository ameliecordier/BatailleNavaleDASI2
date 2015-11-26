import ocean
#A déplacer plus tard dans une classe logique de jeu
def deciderDeJouer():
    print("Bienvenue dans ce jeu de Bataille Navale d'enfer !")
    reponse = input("Voulez-vous jouer avec moi ? (O / N) ")
    
    if reponse == "o":
        print("Youpi")
    elif reponse == "n":
        print("Tant pis")
    else:
        print("Je vous repose la question ?")
        reponse = deciderDeJouer()
    return reponse

#A déplacer plus tard... ? 
def demanderTailleOcean():
    X = initialisationX()
    Y = initialisationY()
    print("Pour info, vous avez demandé un océan de " + str(X) + "x" + str(Y))
    return X, Y

def initialisationX():
    while True:
        try:
            x = int(input("La largeur sera de ? (2 a 50)"))
            if 2<=x<=50:
                break
            else:
                print("Cet entier n'est pas compris entre 2 et 50")
        except ValueError:
              print("Ce n'est pas un entier!")

    return x


def initialisationY():
    while True:
        try:
            y = int(input("La hauteur sera de ? (2 a 50)"))
            if 2<=y<=50:
                break
            else:
                print("Cet entier n'est pas compris entre 2 et 50")
        except ValueError:
              print("Ce n'est pas un entier!")

    return y


def afficherPlateau(oceanTirs, oceanBateaux, largeur, joueur):
    alphabet="  a b c d e f g h i j k l m n o p q r s t u v w x y z"
    print("PLATEAU DE JEU J"+joueur+":")
    print(alphabet[:largeur*2+2])
    oceanTirs.afficherOcean()
    separation = "  "
    for i in range(0, largeur*2-1):
        separation += "-"
    print(separation)
    print(alphabet[:largeur*2+2])
    oceanBateaux.afficherOcean()
    print("")
    separation = ""
    for i in range(0, largeur):
        separation += "/\\"
    print(separation)

#Programme principal
jouer = deciderDeJouer()

if jouer == "o":
    monoceanJ1bateaux = ocean.ocean()
    monoceanJ1tirs = ocean.ocean()
    monoceanJ2bateaux = ocean.ocean()
    monoceanJ2tirs = ocean.ocean()
    tailleX, tailleY = demanderTailleOcean()  

    monoceanJ1bateaux.construireOcean(tailleX, tailleY)
    monoceanJ1tirs.construireOcean(tailleX, tailleY)
    monoceanJ2bateaux.construireOcean(tailleX, tailleY)
    monoceanJ2tirs.construireOcean(tailleX, tailleY)

    afficherPlateau(monoceanJ1tirs,monoceanJ1bateaux,tailleX, "1")



#TEST PAILLARES ^^

#TEST SEVERAC !
    
#ZBLA



