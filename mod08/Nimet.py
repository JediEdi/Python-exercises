nimet = set()
nimi = input ("Tämä ohjelma ottaa kirjoittamasi nimet ja kertoo, onko nimi uusi vai jo valmiiksi osana listaa.\nKirjoita nimi tai paina enteriä nähdäksesi listan nimistä: ")
if nimi != (""):
    nimet.add (nimi)
    print ("Uusi nimi.")
while nimi != (""):
    nimi = input ("Kirjoita nimi tai paina enteriä nähdäksesi listan nimistä: ")
    if nimi in nimet:
        print ("Aiemmin syötetty nimi.")
    else:
        if nimi != (""):
            nimet.add (nimi)
            print ("Uusi nimi.")

for i in nimet:
    print (i)