import math
import time
print ("Tämä ohjelma laskee ensin ympyrän pinta-alan sen säteen perusteella.")
ympyran_sade = input("Ympyrän säde numerona: ")
ympyran_pinta_ala = math.pi * int(ympyran_sade) ** 2 # A = pi * r^2
time.sleep (0.2)
print ("Seuraavaksi lasketaan neliön pinta-ala sivun pituuden perusteella.")
nelion_sivu_a = input("Neliön sivun pituus numerona: ")
nelion_pinta_ala = int(nelion_sivu_a) ** 2 # A = sivu^2
time.sleep (0.5)
print ("¤___________________¤")
time.sleep (0.5)
print (f"Ympyrän pinta_ala: {ympyran_pinta_ala:7.2f}")
print (f"Neliön pinta_ala: {nelion_pinta_ala:7.2f}")
time.sleep (1)
print ("Lasketaan lopuksi suorakulmion pinta-ala sekä piiri.")
suorakulmion_sivu_a = input("Suorakulmion kanta numerona: ")
time.sleep (0.2)
suorakulmion_sivu_b = input("Suorakulmion korkeus numerona: ")
suorakulmion_pinta_ala = int(suorakulmion_sivu_a) * int(suorakulmion_sivu_b) # A = kanta * korkeus
suorakulmion_piiri = int(suorakulmion_sivu_a) * 2 + int(suorakulmion_sivu_b) * 2
time.sleep (0.5)
print ("¤___________________¤")
time.sleep (0.5)
print (f"Suorakulmion pinta_ala: {suorakulmion_pinta_ala:7.2f}")
print (f"Suorakulmion piiri: {suorakulmion_piiri:7.2f}")