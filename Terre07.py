print(" ")
print("             EPREUVE DE LA TERRE : TAILLE D'UNE CHAINE\n         ")

import sys

if len(sys.argv) <= 2 :
    try:
        if sys.argv[1].isdigit() == True:
            print('Entre une chaine de caractère.\nExemple : "Hello Word!"')
        else:        
            prépa = list(sys.argv[1])
            print(len(prépa))
    except IndexError:
        print('Entre une chaine de caractère.\nExemple : "Hello Word!"')        
elif len(sys.argv) > 2 :
    print("Erreur")
else :
    print("Erreur")