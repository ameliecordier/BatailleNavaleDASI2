import Arsenal

class Bateau():

    def __init__(self, arsenal, nom):
        self.arsenal = arsenal
        self.arsenal.ajouterBateau(self)
        self.nom = nom
        self.taille = self.arsenal.dict.get(nom)
