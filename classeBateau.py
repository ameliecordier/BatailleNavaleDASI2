# -*- coding: utf8 -*-

import demandePosBateaux
import classeOcean

class bateau:
    ##Initialisation d'un bateau
    def __init__(self, nom, coord, orien, arsenal):
        self.nomBateau = nom
        self.orientation = orien
        self.posX = ord(coord[0]) - ord('a')

        if len(coord) == 3:
            self.posY = int(coord[1]) * 10 + int(coord[2]) - 1
        else:
            self.posY = int(coord[1]) - 1
        
        self.posX2, self.posY2 = self.getPos2(arsenal)


    ##Fonction getPos2
    ##Retourne les positions x et y du bout du bateau non enregistré
    def getPos2(self, arsenal):        
        if self.orientation == 'h':
            posX2 = self.posX
            posY2 = self.posY - arsenal.tailleBateau[arsenal.nomBateau.index(self.nomBateau)] + 1
        elif self.orientation == 'b':
            posX2 = self.posX
            posY2 = self.posY + arsenal.tailleBateau[arsenal.nomBateau.index(self.nomBateau)] - 1
        elif self.orientation == 'd':
            posX2 = self.posX + arsenal.tailleBateau[arsenal.nomBateau.index(self.nomBateau)] - 1
            posY2 = self.posY
        else: ##if self.orientation == 'g':
            posX2 = self.posX - arsenal.tailleBateau[arsenal.nomBateau.index(self.nomBateau)] + 1
            posY2 = self.posY

        return posX2, posY2


        
##Fonction construitBateaux
##Retourne une liste de 5 bateaux créé par l'utilisateur
def construitListeBateaux(arsenal, oce):
    for i in range(0, len(arsenal.nomBateau)):
        for j in range(0, arsenal.nbBateau[i]):            
            while True:
                print("")
                oce.afficheOcean()
                print("")
                coord, orien = demandePosBateaux.demandeBateau(i + j + 1, arsenal.nomBateau[i])
                bat = bateau(arsenal.nomBateau[i], coord, orien, arsenal)

                if oce.batOk(bat):
                    oceTemp = classeOcean.ocean(oce.longueur, oce.hauteur, oce)
                    oceTemp.ajouteBateau(bat)
                    
                    if oceTemp.validationBateau():
                        break
            
            oce.ajouteBateau(bat)
            print("")
