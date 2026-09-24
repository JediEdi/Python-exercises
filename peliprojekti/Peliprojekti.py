custom_nimet = set()
pelaajan_nimi = ("Testeri") # DEBUG - LAITA POIS LOPULLISESSA VERSIOSSA
pelaajan_ika = 20 # DEBUG - LAITA POIS LOPULLISESSA VERSIOSSA

def paavalikko():
    numerovalinta = input ("\nMinkä komennon haluatte suorittaa?\n1: Pelaa peliä\n2: Asetukset\n3: Poistu pelistä\nVastaus: ")

    if numerovalinta == "1":
        return custom_nimet, numerovalinta

    elif numerovalinta == "2":
        custom_nimet.add(input("Nimi: "))
        return custom_nimet, numerovalinta
    elif numerovalinta == "3":
        print ("\nMoro.")

print ("Tervetuloa Evoluutiomiehen maailmaan.")
# pelaajan_nimi = input("Mikä on nimenne?\nVastaus: ") # DEBUG - LAITA PÄÄLLE LOPULLISESSA VERSIOSSA
# pelaajan_ika = int(input("Mikä on ikänne?\nVastaus kokonaislukuna: ")) # DEBUG - LAITA PÄÄLLE LOPULLISESSA VERSIOSSA
print (f"\nPelaajan nimi: {pelaajan_nimi} \nPelaajan ikä: {pelaajan_ika} ")
if pelaajan_ika < 12:
    print ("\nOlette alaikäinen. Ette voi pelata.")
else:
    custom_nimet, numerovalinta = paavalikko()
    if numerovalinta == "1":
        print ("Peli alkaa")
        print (custom_nimet)
    elif numerovalinta == "2":
        print ("Asetukset...")
        print (custom_nimet)
    elif numerovalinta == "3":
        print ("Poistuit pelistä")