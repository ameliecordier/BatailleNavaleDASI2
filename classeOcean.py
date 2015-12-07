# -*- coding: utf8 -*-

class ocean:
    ##Initialisation d'un océan
    def __init__(self, x, y, oce=None):
        self.longueur = x
        self.hauteur = y
        self.listeBateau = []

        if oce == None:
            self.grille = self.construitOcean()
        else:
            self.grille = self.copyGrille(oce.grille)


    ##Fonction construitOcean
    ##Retourne un tableau d'"o" de longueur x et de largeur y
    def construitOcean(self): 
        oce = []
        
        for x in range(0, self.longueur):
            oce.append([])
            
            for y in range(0, self.hauteur):
                oce[x].append('o')

        return oce    


    ##
    def copyGrille(self, grille): 
        oce = []
        
        for x in range(0, self.longueur):
            oce.append([])
            
            for y in range(0, self.hauteur):
                oce[x].append(grille[x][y])

        return oce


    ##Procedure afficheOcean
    ##Affiche l'océan passé en paramètre
    def afficheOcean(self):
        chaine = '   '
        
        for x in range(0, self.longueur):
            chaine = chaine + chr(x + ord('a')) + ' '
            
        print(chaine)
                
        for y in range(0, self.hauteur):
            chaine = str(y + 1) + ' '
            
            if y < 9:
                chaine = ' ' + chaine
            
            for x in range(0, self.longueur):
                chaine = chaine + self.grille[x][y] + ' '
                
            print(chaine)


    ##Procedure ajouteBateau
    ##Ajoute les bateaux du paramètre dans l'océan
    def ajouteBateau(self, bat):
        self.listeBateau.append(bat)
        
        if bat.posX <= bat.posX2 + 1:
            px = bat.posX
            px2 = bat.posX2 + 1
        else:
            px = bat.posX2
            px2 = bat.posX + 1
            
        if bat.posY <= bat.posY2 + 1:
            py = bat.posY
            py2 = bat.posY2 + 1
        else:
            py = bat.posY2
            py2 = bat.posY + 1
        
        for y in range(py, py2):
            for x in range(px, px2):
                self.grille[x][y] = 'x'


    ##Fonction batOk
    ##Test si le bateau n'est pas à cheval sur un autre
    def batOk(self, bat):
        if bat.posX <= bat.posX2 + 1:
            px = bat.posX
            px2 = bat.posX2 + 1
        else:
            px = bat.posX2
            px2 = bat.posX + 1
            
        if bat.posY <= bat.posY2 + 1:
            py = bat.posY
            py2 = bat.posY2 + 1
        else:
            py = bat.posY2
            py2 = bat.posY + 1

        if px < 0 or py < 0:
            print("Les bateaux ne peuvent pas sortir de l'océan !")
            return False              

        try:
            for y in range(py, py2):
                for x in range(px, px2):
                    if self.grille[x][y] == 'x':
                        print('Les bateaux ne peuvent pas se croiser !')
                        return False
        except IndexError:
            print("Les bateaux ne peuvent pas sortir de l'océan !")
            return False            
                
        return True


    ##Fonction batOk
    def validationBateau(self):
        self.afficheOcean()

        while True:
            rep = input("Validez-vous l'emplacement de ce bateau ? (o/n) : ")
            
            if not (rep == "o" or rep == "n" or rep == "O" or rep == "N"):
                print("Vous ne pouvez répondre que oui ou non !")
            elif rep == "O" or rep == "o":
                return True
            elif rep == "N" or rep == "n":
                return False
