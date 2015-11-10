import Ocean
import Bateau

class Main():
    
    monocean = Ocean.Ocean()
    jouer = monocean.introJeu()
    if jouer == "O":
        ligne = []
        ocean = []
        tailleX, tailleY = monocean.demanderTailleOcean()
        monocean.creerOcean(tailleX,tailleY)
        monocean.afficherOcean(ocean)
