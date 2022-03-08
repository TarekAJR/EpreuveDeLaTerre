print(" ")
print("             EPREUVE DE LA TERRE : PAIRE OU IMPAIRE\n         ")

import sys


if len(sys.argv) >= 2 :
    try:
        if (int(sys.argv[1]) % 2) == 0:
	        print("Paire")
        elif (int(sys.argv[1]) % 2) == 1:
	        print("Impaire")
    except ValueError:
        print("Tu ne me la mettras pas a l'envers MECTON.")
elif len(sys.argv) == 1 :
    print("Tu ne me la mettras pas a l'envers MECTON.")
