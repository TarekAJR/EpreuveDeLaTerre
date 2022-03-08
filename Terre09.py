print(" ")
print("             EPREUVE DE LA TERRE : RACINE CARRÉE D'UN NOMBRE\n         ")

import sys

if len(sys.argv) <= 2 :
    try:
        if sys.argv[1].isdigit() == True:
            print("Résultat : {}".format(int((sys.argv[1])) ** 2 ))
        else:        
            print('Entre deux nombres positifs')
    except IndexError:
        print('Entrer un nombre pour calculer sa racine carée')        
elif len(sys.argv) > 2 :
    print("Erreur")
else :
    print("Erreur")
