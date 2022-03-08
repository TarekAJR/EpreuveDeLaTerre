print(" ")
print("             EPREUVE DE LA TERRE : TERRE OK\n         ")

import sys

if len(sys.argv) <= 2 :
    try:
        if sys.argv[1].isdigit() == False:
            print("J'ai terminé l'Épreuve de la Terre et c'était {} :)".format(sys.argv[1]))
        else:        
            print('Entre un adjectif de votre choix (Facile ?)')
    except IndexError:
        print('Entre un adjectif de votre choix (Facile ?)')       
elif len(sys.argv) > 2 :
    print("Erreur")