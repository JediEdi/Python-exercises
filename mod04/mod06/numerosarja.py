luvut = []
luku = float(input ("Tämä ohjelma ottaa kirjoittamasi luvut ja näyttää niistä pienimmän ja suurimman.\nKirjoita luku tai paina enteriä nähdäksesi pienimmän ja suurimman luvun: "))
luvut.append (luku)
while luku != (""):
    luku = input ("Kirjoita luku tai paina enteriä nähdäksesi pienimmän ja suurimman luvun: ")
    if luku != (""):
        luku = float(luku)
        luvut.append (luku)
luvut.sort()
pienin = (luvut[0])
suurin = (len(luvut) - 1)
print (luvut[pienin])
print (luvut[suurin])
# Muuta floateiksi kaikki, paitsi "". Huh huh.