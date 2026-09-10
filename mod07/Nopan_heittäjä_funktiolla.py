import random
def nopan_heitto():
    silmaluku = random.randint (1, 6)
    print (silmaluku)
    return silmaluku
silmaluku = nopan_heitto()
while silmaluku != 6:
    silmaluku = nopan_heitto()
print ("Voitto!")