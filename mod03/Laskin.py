import time
print("Tämä ohjelma laskee kolmen antamasi kokonaisluvun summan, tulon ja keskiarvon.")
time.sleep (1)
numero_a = int(input("Ensimmäinen kokonaisluku: "))
numero_b = int(input("Toinen kokonaisluku: "))
numero_c = int(input("Kolmas kokonaisluku "))
summa = numero_a + numero_b + numero_c
tulo = numero_a * numero_b * numero_c
keskiarvo = summa / 3
time.sleep (0.5)
print ("¤___________________¤")
time.sleep (0.5)
print ("Lukujen summa: " + str(summa))
print ("Lukujen tulo: " + str(tulo))
print ("Lukujen keskiarvo: " + str(keskiarvo))