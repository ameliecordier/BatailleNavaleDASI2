# -*- coding: utf-8 -*-

import flotte

print("Bienvenue dans ce jeu de bataille navale")

monBateau = flotte.Bateau()
monBateau.name = "Hermione"
monBateau.size = 5

monAutreBateau = flotte.Bateau()
monAutreBateau.configure("porte-avion")

encoreUnBateau = flotte.Bateau()
encoreUnBateau.configure("radeau")

print(monBateau)
print(monAutreBateau)
print(encoreUnBateau)

