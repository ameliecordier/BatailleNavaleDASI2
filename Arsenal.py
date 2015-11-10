class Arsenal():

    def __init__(self):
        self.bateaux = []
        self.creerDictionnaire()
        self.arsenal = None


    def creerDictionnaire(self):
        self.dict = dict()
        self.dict["PorteAvion"] = 5
        self.dict["Radeau"] = 1
        self.dict["Torpilleur"] = 3
        self.dict["SuperTorpilleur"] = 4
        self.dict["SousMarin"] = 6

    def ajouterBateau(self,bateau):
        self.bateaux.append(bateau)
