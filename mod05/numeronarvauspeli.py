import random
luku = random.randint (1, 10)
arvaus = int(input ("Tämä ohjelma on arponut kokonaisluvun yhden ja kymmenen välillä. Heitä arvaus.\nArvaus kokonaislukuna: "))
while arvaus != luku:
    if arvaus < luku:
        arvaus = int(input ("Arvauksesi oli liian pieni! Yritä uudelleen.\nArvaus kokonaislukuna: "))
    if arvaus > luku:
        arvaus = int(input ("Arvauksesi oli liian suuri! Yritä uudelleen.\nArvaus kokonaislukuna: "))
print ("Oikein!")