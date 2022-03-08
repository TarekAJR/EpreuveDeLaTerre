print(" ")
print("             EPREUVE DE LA TERRE : Trié ou pas\n         ")

import sys

try:
    test_list = list(map(int, sys.argv[1:]))
    if sys.argv[1].isdigit() == True:
        flag = 0
        if(all(test_list[i] <= test_list[i + 1] for i in range(len(test_list)-1))):
            flag = 1
            
        if (flag) :
            print ("Triée !")
        else :
            print ("Pas Triée !")
    else:
        print('Entre une chaine de caractère.\nExemple : "Hello Word!"')
except ValueError:
    print('Erreur, Entre au moin 3 chiffres. Exemple : 3 8 9 12')