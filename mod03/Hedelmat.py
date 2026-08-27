import time
print("Tämä ohjelma laskee hedelmien hinnan kilogrammojen mukaan.")
time.sleep (1)
banaanin_hinta_kilogrammoina = 2.85
omenan_hinta_kilogrammoina = 3.15
appelsiinin_hinta_kilogrammoina = 4.05
numero_a = float(input("Banaanien paino kilogrammoina: "))
numero_b = float(input("Omenoiden paino kilogrammoina: "))
numero_c = float(input("Appelsiinien paino kilogrammoina: "))
print ("Banaanien hinta: " + str((numero_a * banaanin_hinta_kilogrammoina)))
print ("Omenoiden hinta: " + str((numero_b * omenan_hinta_kilogrammoina)))
print ("Appelsiinien hinta: " + str((numero_c * appelsiinin_hinta_kilogrammoina)))
time.sleep (0.5)
print ("¤___________________¤")
time.sleep (0.5)
print ("Hinta yhteensä: " + str(numero_a * banaanin_hinta_kilogrammoina + numero_b * omenan_hinta_kilogrammoina + numero_c * appelsiinin_hinta_kilogrammoina))