import time
senttimetri = 1
tuuma = (senttimetri * 2.54)
luku = float(input ("Tämä ohjelma laskee, kuinka monta senttimetriä antamasi pituus on tuumina.\nPituus tuumina: "))
while luku >=0:
    time.sleep (0.5)
    print ("¤___________________¤")
    time.sleep (0.5)
    print ("Luku senttimetreinä: " + str(luku * tuuma))
    time.sleep (0.2)
    luku = float(input ("\nPituus tuumina: "))