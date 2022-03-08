print(" ")
print("             EPREUVE DE LA TERRE : PUISSANCE D'UN NOMBRE\n         ")

import sys

if len(sys.argv) <= 3 :
    try:
        if sys.argv[1].isdigit() == True and sys.argv[2].isdigit() == True:
            print("Résultat : {}".format(int((sys.argv[1])) ** int((sys.argv[2]))))
        else:        
            print('Entre deux nombres positifs')
    except IndexError:
        print('Entre deux nombres pour un calcul de puissance \nExemple : 2 3')        
elif len(sys.argv) > 3 :
    print("Erreur")
else :
    print("Erreur")