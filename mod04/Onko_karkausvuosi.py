import time
print ("Tämä ohjelma laskee, onko antamasi vuosi karkausvuosi.")
time.sleep (1)
vuosi = int(input("Minkä vuoden tahdot analysoida?.\nVastaus kokonaislukuina: "))
jakojaannos_4 = (vuosi % 4)
jakojaannos_100 = (vuosi % 100)
jakojaannos_400 = (vuosi % 400)
if jakojaannos_4 == 0:
    print ("Annettu vuosiluku on karkausvuosi.")
elif jakojaannos_100 == 0 and jakojaannos_400 == 0:
    print ("Annettu vuosiluku on karkausvuosi.")
else:
    print ("Annettu vuosiluku ei ole karkausvuosi.")