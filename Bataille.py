print("Bienvenue dans ce jeu de Bataille Navale !")
reponse = input("Voulez-vous jouer avec moi ? (O/N) ")

if reponse == "O":
    print("Let's go !")
    x = input("Quelle est la valeur de X ? ")
    y = input("Quelle est la valeur de Y ? ")
    print("Valeur de x : " + x + "\nValeur de y : " + y)
    ligne = []
    ocean = []
    i=0
    for i in range (0,int(x)):
        ligne.append("O")
        
    for i in range (0,int(y)):
        ocean.append(ligne)

    for i in range (0,int(y)):
         print(" ".join(ocean[i]))
    
   

else:
    print("Oh noooon...")

