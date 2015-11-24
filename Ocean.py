class ocean:

    def __init__(self):
        self.ocean = []
    
    def construireOcean(self, x, y):
        ligne = []
        for i in range(0, x):
            ligne.append("o")
        for i in range(0, y):        
            self.ocean.append(ligne)

    def afficherOcean(self):
        for i in range(0,len(self.ocean)):
           print(" ".join(self.ocean[i]))

    def largeurOcean(self):
        return len(self.ocean)

    def hauteurOcean(self):
        return len(self.ocean[0])        
        
monocean = ocean()
monocean.construireOcean(4, 3)
monocean.afficherOcean()
print(monocean.largeurOcean())
print(monocean.hauteurOcean())
