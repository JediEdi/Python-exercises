import random
def nopan_heitto(tahkot):
    silmaluku = random.randint (1, tahkot)
    print (silmaluku)
    return silmaluku
tahkot = int(input ("Tämä ohjelma heittää noppaa, kunnes saa suurimman mahdollisen silmäluvun. Minkä luvun haluat nopan suurimmaksi mahdolliseksi silmäluvuksi?\nVastaus kokonaislukuina: "))
silmaluku = nopan_heitto(tahkot)
while silmaluku != (tahkot):
    silmaluku = nopan_heitto(tahkot)
print ("Voitto!")