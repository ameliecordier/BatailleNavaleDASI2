# -*- coding: utf-8 -*-

# C'est pas moi, c'est wikipedia :https://fr.wikipedia.org/wiki/Bataille_navale_%28jeu%29
typesBateaux = {
    "porte-avion":5,
    "croiseur":4,
    "contre-torpilleurt":3,
    "sous-marin":3,
    "torpilleur":2
}


class Bateau:
    name = ""
    size = 0

    def __str__(self):
        return "Je m'appelle " + self.name + " et je mesure " + str(self.size) + " unité(s) !" 



    def configure(self, name):
        self.name = name
        self.size = typesBateaux[name]


