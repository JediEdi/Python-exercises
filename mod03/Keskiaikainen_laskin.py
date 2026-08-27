import time
import math
print("Tämä ohjelma muuntaa antamasi keskiaikaiset massan suureet kilogrammoiksi ja grammoiksi.")
time.sleep (1)
numero_a = float(input("Paino leivisköinä: "))
numero_b = float(input("Paino nauloina: "))
numero_c = float(input("Paino luoteina: "))
kilogramma = 1
gramma = kilogramma * 0.001
luoti = gramma * 13.3
naula = luoti * 32
leiviska = naula * 20
massa_kilogrammoina = math.floor(numero_a * leiviska + numero_b * naula + numero_c * luoti) # Pyöristetään alaspäin.
massa_grammoina = (numero_a * leiviska + numero_b * naula + numero_c * luoti - massa_kilogrammoina) * 1000 # Ei pyöristetä. Miinustetaan kilogrammat. If it works, it works.
time.sleep (0.5)
print ("¤___________________¤")
time.sleep (0.5)
print (f"Massa kilogrammoina ja grammoina: {massa_kilogrammoina:7.0f} kilogrammaa, {massa_grammoina:7.2f} grammaa")
# massa_raaka = numero_a * leiviska + numero_b * naula + numero_c * luoti
# print ("Massa sellaisenaan: " + str(massa_raaka))