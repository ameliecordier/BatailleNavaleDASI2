# -*- coding: utf-8 -*-

class arsenal:
    def __init__(self):
        self.nomBateau = ['porte-avions', 'croiseur', 'contre-torpilleurs', 'sous-marin', 'torpilleur']
        self.tailleBateau = [5, 4, 3, 3, 2]
        self.nbBateau = [1, 1, 1, 1, 1]


    def nombreBateau(self):
        res = 0;
        
        for i in range(0, len(self.nbBateau)):
            res = res + self.nbBateau[i]

        return res
