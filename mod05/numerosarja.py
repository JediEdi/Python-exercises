luvut = []
luku = input ("Tämä ohjelma ottaa kirjoittamasi luvut ja näyttää niistä pienimmän ja suurimman.\nKirjoita luku tai paina enteriä nähdäksesi pienimmän ja suurimman luvun: ")
if luku != (""):
    luku = float(luku)
    luvut.append (luku)
else:
    print ("Et antanut lukuja. Tässä on sinulle mukava virheilmoitus:")
while luku != (""):
    luku = input ("Kirjoita luku tai paina enteriä nähdäksesi pienimmän ja suurimman luvun: ")
    if luku != (""): # Muuta floateiksi kaikki, paitsi "".
        luku = float(luku)
        luvut.append (luku)
luvut.sort()
pienin = (luvut[0])
suurin = (luvut[(len(luvut)) - 1])
print ("Pienin luku: " + str(pienin))
print ("Suurin luku: " + str(suurin))