print("Bienvenue dans ce jeu de Bataille Navale d'enfer !")
reponse = input("Voulez-vous jouer avec moi ? (O / N) ")

if reponse == "O":
    print("Youpi, let's go !")
    X = input("Quel est la taille de X")
    Y = input("Quel est la taille de Y")
    print("La valeur de X est : " + X + " et la valeur de Y est " + Y)

    ligne = []
    ocean = []

    for i in range(0,int(X)):
        ligne.append("o")

    for i in range(0,int(Y)):
        ocean.append(ligne)

    for i in range(0,int(Y)):
        print(" ".join(ocean[i]))
else:
    print("Oh noooon... personne ne veut jamais jouer avec moi !")


l = []
l.append("toto")
l.append("tata")
print(",".join(l))

print(" ".join(l))
