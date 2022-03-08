print(" ")
print("             EPREUVE DE LA TERRE : NOMBRE PREMIER\n         ")

import sys

if len(sys.argv) <= 2 :
    try:
        if sys.argv[1].isdigit() == True:
            if int(sys.argv[1]) < 2 :
                print("Non, {} n'est pas un nombre premier".format(sys.argv[1]))
            for i in range(2, int(sys.argv[1])):
                if int(sys.argv[1]) % i == 0:
                    print("Non, {} n'est pas un nombre premier".format(sys.argv[1]))
                    break
            else:
                print("Oui, {} est un nombre premier".format(sys.argv[1]))
        else:        
            print('Entre un nombre positif')
    except IndexError:
        print("Entrer un nombre pour savoir s'il est premier")        
elif len(sys.argv) > 2 :
    print("Erreur")



