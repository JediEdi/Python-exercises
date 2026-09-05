jaolliset = []
luku = 0
while luku < 1000:
    if (luku % 3 == 0):
        jaolliset.append (luku)
    luku = (luku + 1)
print ("Tämä ohjelma laskee yhden ja tuhannen välillä luvut, jotka ovat jaollisia kolmella:\n " + str(jaolliset))