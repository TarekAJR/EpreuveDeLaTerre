print(" ")
print("             EPREUVE DE LA TERRE : ALPHABET A PARTIR DE\n         ")

import sys

Départ = sys.argv[1]                        #Recupere la lettre entrée en paramètre
i = 0

Alphabet = list(map(chr, range(97, 123)))   #Recupere l'alphabet(ASCI) dans une liste
for Lettre in Alphabet:                     #Boucler sur tout les occurances de la liste
    if Départ in Alphabet:                  #Condition pour retrouver la lettre dans la liste
        i = Alphabet.index(Départ)          #Nommer variable qui gardera l'index de la lettre
final = "".join(Alphabet[i:])               #Nommer Varible du rendu final sans les espaces
print(final)

