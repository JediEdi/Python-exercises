import random
kuutiot = int(input ("Tämä ohjelma heittää arpakuutioita ja laskee niiden summan. Kuinka monta arpakuutiota heitetään?\nVastaus kokonaislukuna: "))
summa = 0
for heitto in range(1, (kuutiot + 1)):
    summa = summa + random.randint (1, 6)
print (summa)