print(" ")
print("             EPREUVE DE LA TERRE : INVERSER UNE CHAINE\n         ")

import sys

if len(sys.argv) >= 2 :
    if sys.argv[1].isdigit() == True:
        print('Entre une chaine de caractère.\nExemple : "Hello Word!"')
    else:
        prépa = list(reversed(sys.argv[1]))
        print(''.join(prépa))
else:
    print("Erreur")