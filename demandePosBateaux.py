# -*- coding: utf8 -*-

##Fonction demandeBateau
##Retourne les coordonnées et la position du bateau rentrée au clavier
def demandeBateau(i, nomBateau):
    while True:
        coord = input("Position du " + str(i) + "e bateau (" + nomBateau + ") : ")
    
        try:
            assert (len(coord) == 2 or len(coord) == 3) and coord[0].isalpha() and coord[1].isdigit()

            if len(coord) == 3:
                assert coord[2].isdigit()
            
            print("Orientation du " + str(i) + "e bateau ?")
            orien = input("\tdroite : d\n\tgauche : g\n\thaut : h\n\tbas : b\n")
    
            if orien == 'D':
                orien = 'd'
            elif orien == 'G':
                orien = 'g'
            elif orien == 'H':
                orien = 'h'
            elif orien == 'B':
                orien = 'b'
            elif orien != 'd' and orien != 'g' and orien != 'h' and orien != 'b':
                raise ValueError('Orientation invalide.')

            return coord, orien
        except AssertionError:
            print("Une coordonnée n'est composée que d'une lettre et d'un ou deux chiffres !")
        except ValueError as err:
            print(err.args[0])
