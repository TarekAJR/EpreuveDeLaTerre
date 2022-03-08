print(" ")
print("             EPREUVE DE LA TERRE : 12 TO 24\n         ")

import sys

separateur = ":"
am = " AM"
pm = " PM"

Parametre = sys.argv[1].split(separateur)
#print(Parametre)
h = int(Parametre[0])
#print(h)
m = Parametre[1]
#print(m)cd
restitution = int()
final = str()

if len(sys.argv) <= 2 :
    try:
        if (0 <= int(m) <= 59):
            if (0 <= h < 25):
                if ( 0 <= h <= 12 ):
                    restitution = h + 12
                    final = str(restitution) + separateur + m + pm
                    print(final)

                elif (13 <= h <= 24):
                    final = str(restitution)+ separateur + m + am
                    print(final)
            else:        
                print('Entre un horraire existant.\nExemple : 23:40')
        else:
            print('Entre un horraire existant.\nExemple : 23:40')
    except IndexError:
        print('Entre un horraire.\nExemple : 23:40')        
elif len(sys.argv) > 3 :
    print("Erreur")
else :
    print("Erreur")