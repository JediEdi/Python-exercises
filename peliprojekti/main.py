custom_nimet = set()
pelaajan_nimi = ("Testeri") # DEBUG - LAITA POIS LOPULLISESSA VERSIOSSA
pelaajan_ika = 20 # DEBUG - LAITA POIS LOPULLISESSA VERSIOSSA

def paavalikko():
    numerovalinta = input ("\nMinkä komennon haluatte suorittaa?\n1: Pelaa peliä\n2: Asetukset\n3: Poistu pelistä\nVastaus: ")

    if numerovalinta == "1":
        return numerovalinta, custom_nimet

    elif numerovalinta == "2":
        custom_nimet.add(input("Nimi: "))
        return numerovalinta, custom_nimet
    elif numerovalinta == "3":
        print ("\nMoro.")
        return numerovalinta, custom_nimet

print ("Tervetuloa Evoluutiomiehen maailmaan.")
# pelaajan_nimi = input("Mikä on nimenne?\nVastaus: ") # DEBUG - LAITA PÄÄLLE LOPULLISESSA VERSIOSSA
# pelaajan_ika = int(input("Mikä on ikänne?\nVastaus kokonaislukuna: ")) # DEBUG - LAITA PÄÄLLE LOPULLISESSA VERSIOSSA
print (f"\nPelaajan nimi: {pelaajan_nimi} \nPelaajan ikä: {pelaajan_ika} ")
if pelaajan_ika < 12:
    print ("\nOlette alaikäinen. Ette voi pelata.")
else:
    numerovalinta, custom_nimet = paavalikko()
    while numerovalinta == "2":
        numerovalinta, custom_nimet = paavalikko()
    if numerovalinta == "1":
        print (custom_nimet)
        from esineet import Esine
        from huoneet import Huone, Tyhja
        from mekanismit import Mekanismi
        from pelaaja import Pelaaja
        tyhja = Tyhja()
        huone_2_3 = Huone("Käytävä", tyhja, tyhja, tyhja, tyhja)
        huone_2_2 = Huone("Aloitus", huone_2_3, tyhja, tyhja, tyhja)
        kartta = Esine("Kartta", 0.2)
        huone_2_2.lisaa_esine(kartta)
        pelaaja = Pelaaja("Testeri", huone_2_2)
        pelaaja.katso_ymparille()
        pelaaja.liiku("N")
        pelaaja.katso_ymparille()
        pelaaja.liiku("N")