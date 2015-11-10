import Main

class Ocean():
    
    def afficherOcean(ocean,self):
        for i in range (0,len(ocean)):
             print(" ".join(ocean[i]))

    def demanderTailleOcean(self):
        x = input("Quelle est la valeur de X ? ")
        y = input("Quelle est la valeur de Y ? ")
        print("Valeur de x : " + x + "\nValeur de y : " + y)
        return int(x), int(y)

    def creerOcean(self,x,y):
        i=0
        for i in range (0,int(x)):
            ligne.append("O")
        
        for i in range (0,int(y)):
            ocean.append(ligne)
        
    def introJeu(self):
        print("Bienvenue dans ce jeu de Bataille Navale !")
        reponse = input("Voulez-vous jouer avec moi ? (O/N) ")    
        if reponse == "O":
            print("Let's go !")
        elif reponse == "N":
            print("Oh noooooon..")
        else:
            print("Je n'ai pas compris votre choix !")
            reponse = introJeu()
        return reponse

