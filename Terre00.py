#coding:utf-8

print(" ")
print("             EPREUVE DE LA TERRE : L'ALPHABET\n         ")

# LA MÉTHODE SANS LA BOUCLE PERMETTANT DE D'OBTENIR LE RESULTAT SANS LA BOUCLE

def listAlphabet():
# ON UTLISER ICI UNE FONCTION QUI PARCOURT LES CARACTÈRE ASCII L'ALPHABET QUI COMMENCE AU CARACTÈRE 97
    return list(map(chr, range(97, 123)))

rendu = ' '.join(listAlphabet())
sansespace = rendu.replace(" ","")
print(sansespace)
print("\n")

# LA MÉTHODE AVEC LA BOUCLE HONNETEMENT J'AI DEAD SA
for i in list(map(chr, range(97, 123))):
    print(i, end="")
# SUIVIE D'UN RETOUR A LA LIGNE
print("")