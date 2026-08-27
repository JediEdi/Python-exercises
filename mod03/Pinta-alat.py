import math
import time
print ("Tämä ohjelma laskee ensin ympyrän pinta-alan sen säteen perusteella.")
sade = input("Ympyrän säde numerona: ")
ympyra = math.pi * int(sade) ** 2 # A = pi * r^2
time.sleep (1)
print ("Seuraavaksi lasketaan neliön pinta-ala sivun pituuden perusteella.")
sivu = input("Neliön sivun pituus numerona: ")
nelio = int(sivu) ** 2 # A = sivu^2
time.sleep (0.5)
print ("¤-------------------¤")
time.sleep (0.5)
print (f"Ympyrän pinta-ala: {ympyra:7.2f}")
print (f"Neliön pinta-ala: {nelio:7.2f}")