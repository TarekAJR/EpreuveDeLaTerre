print(" ")
print("             EPREUVE DE LA TERRE : DIVISIONS\n         ")

import sys


Nombre1 = sys.argv[1]
Nombre2 = sys.argv[2]
Nombre1 = int(Nombre1)
Nombre2 = int(Nombre2)

if Nombre1 >= Nombre2:
    try:
        print("Résultat : {}".format(Nombre1 / Nombre2))
        print("Reste : {}".format(Nombre1 % Nombre2))
    except ZeroDivisionError:
        print("Erreur")
else:
    print("Erreur")
