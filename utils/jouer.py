class Jouer:

    reponse = ""
    def __init__(self):

    def deciderDeJouer():
        print("Bienvenue dans ce jeu de Bataille Navale d'enfer !")
        self.reponse = input("Voulez-vous jouer avec moi ? (O / N) ")
    
        if self.reponse == "O":
            print("Youpi")
        elif self.reponse == "N":
            print("Tant pis")
        else:
            print("Je vous repose la question ?")
            self.reponse = deciderDeJouer()
        return self.reponse
