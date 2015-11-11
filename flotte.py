# -*- coding: utf-8 -*-

class Bateau:
    name = ""
    size = 0

    def __str__(self):
        return "Je m'appelle " + self.name + " et je mesure " + str(self.size) + " unité(s) !" 




    def configure(self, name):
        self.name = name
        if name == "porte-avion":
            self.size = 5
        else:
            self.size = 1


