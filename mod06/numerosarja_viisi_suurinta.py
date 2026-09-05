luvut = []
luku = input ("Tämä ohjelma ottaa kirjoittamasi luvut ja näyttää niistä viisi suurinta.\nKirjoita luku tai paina enteriä nähdäksesi viisi suurinta lukua suurimmasta alkaen: ")
if luku != (""):
    luku = float(luku)
    luvut.append (luku)
else:
    print ("Et antanut lukuja. Tässä on sinulle mukava virheilmoitus:")
while luku != (""):
    luku = input ("Kirjoita luku tai paina enteriä nähdäksesi viisi suurinta lukua suurimmasta alkaen: ")
    if luku != (""): # Muuta floateiksi kaikki, paitsi "".
        luku = float(luku)
        luvut.append (luku)
luvut.sort(reverse=True)
print (luvut[0:5])