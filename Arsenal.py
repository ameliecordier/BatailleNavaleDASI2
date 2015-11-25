class Arsenal():

    def __init__(self):
        self.bateaux = []
        self.creerDictionnaire()
        self.arsenal = None


    def creerDictionnaire(self):
        self.dict = dict()
        self.dict["Radeau"] = 1
        self.dict["Torpilleur"] = 2
        self.dict["Sous-marin"] = 3
        self.dict["Contre-torpilleur"] = 3
        self.dict["Croiseur"] = 4
        self.dict["Porte-avion"] = 5

    def ajouterBateau(self,bateau):
        self.bateaux.append(bateau)
