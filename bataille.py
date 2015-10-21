import unittest


#Propre
def afficherOcean(ocean):
    for i in range(0,len(ocean)):
       print(" ".join(ocean[i]))

def construireLigne(x):
    for i in range(0, x):
        ligne.append("o")
    return ligne    

def construireOcean(x, y):
    l = construireLigne(x)
    for i in range(0, y):        
        ocean.append(l)
    return ocean

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

def demanderTailleOcean():
    X = input("Quel est la taille de X ? ")
    Y = input("Quel est la taille de Y ? ")
    print("Pour info, vous avez demandé un océan de " + X + "x" + Y)
    return int(X), int(Y)

#Programme principal
ligne = [] # A refactorer la prochaine fois... parce que c'est pas top
ocean = []
jouer = deciderDeJouer()
if jouer == "O":
    tailleX, tailleY = demanderTailleOcean()
    ocean=construireOcean(tailleX, tailleY)    
    afficherOcean(ocean)



class TestBatailleMethods(unittest.TestCase):

    def test_constructionOcean(self):
        monOcean = construireOcean(3,7)
        self.assertEqual(len(monOcean),7)
        self.assertEqual(len(monOcean[0]),3)

  
unittest.main()

