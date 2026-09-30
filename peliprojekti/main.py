custom_nimet = []
pelaajan_nimi = ("Testeri") # DEBUG - LAITA POIS LOPULLISESSA VERSIOSSA
pelaajan_ika = 20 # DEBUG - LAITA POIS LOPULLISESSA VERSIOSSA

def paavalikko():
    numerovalinta = input ("\nMinkä komennon haluatte suorittaa?\n1: Pelaa peliä\n2: Asetukset\n3: Poistu pelistä\nVastaus: ")

    if numerovalinta == "1":
        return numerovalinta, custom_nimet

    elif numerovalinta == "2":
        custom_nimet.append(input("Nimi: "))
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
    numerovalinta = "1" # DEBUG - LAITA POIS LOPULLISESSA VERSIOSSA
    custom_nimet = ["Testeri2", "Testeri3", "Testeri4"] # DEBUG - LAITA POIS LOPULLISESSA VERSIOSSA
    # numerovalinta, custom_nimet = paavalikko() # DEBUG - LAITA PÄÄLLE LOPULLISESSA VERSIOSSA
    while numerovalinta == "2":
        numerovalinta, custom_nimet = paavalikko()
    if numerovalinta == "1":
        print (custom_nimet)
        from esineet import Esine, Luettava
        from huoneet import Huone, Tyhja
        from mekanismit import Mekanismi
        from pelaaja import Pelaaja
        import random
        rami = ("Rami")
        tyhja = Tyhja()
        huone_2_3 = Huone("Käytävä", tyhja, tyhja, tyhja, tyhja)
        huone_2_2 = Huone("Aloitus", huone_2_3, tyhja, tyhja, tyhja)

        nappi = Mekanismi("Nappi")
        if random.randint(1, 2) == 1:
            indeksi = random.randint (1, (len(custom_nimet) - 1))
            rami = custom_nimet[indeksi]
        kartta = Luettava("Kartta", 0.2, (f"Kartassa lukee: 'Kartta on keskeneräinen. ASCII kartta tulossa, ehkä. Tämän kirjoitti {rami}'"))

        huone_2_2.lisaa_esine(kartta)
        huone_2_2.lisaa_mekanismi(nappi)
        pelaaja = Pelaaja(pelaajan_nimi, huone_2_2)
        while 1 == 1:
            pelaaja.valikko()