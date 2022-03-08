print(" ")
print("             EPREUVE DE LA TERRE : Trouver la Suisse (LOL)\n         ")

import sys

if len(sys.argv) <= 4 :
    try:
        if sys.argv[1].isdigit() == True and sys.argv[2].isdigit() == True and sys.argv[3].isdigit() == True:
            if sys.argv[1] != sys.argv[2] != sys.argv[3]:
                list_int = list(map(int, sys.argv[1:]))
                list_int.sort()
                print(list_int[1])
            else:
                print('Entre 3 chiffres différents.\nExemple : 11 40 34')
        else:
            print('Entre 3 chiffres différents.\nExemple : 11 40 34')
    except IndexError:
        print('Entre 3 chiffres différents.')        
elif len(sys.argv) > 5 :
    print("Erreur")
else :
    print("Erreur")