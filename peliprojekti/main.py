
# with open ("ohjeet.txt", "r", encoding="utf-8") as tiedosto: # DEBUG - LAITA PÄÄLLE LOPULLISESSA VERSIOSSA
#     data = tiedosto.read()
#     print (data)
# input ("Kirjoittakaa jotain, jos olette ymmärtäneet ohjeet: ")

# with open ("intro.txt", "r", encoding="utf-8") as tiedosto:
#     data = tiedosto.read()
#     print (data)
# input ("Kirjoittakaa jotain, jos haluatte vihdoin peliin: ")

def paavalikko():
    numerovalinta = input ("\nMinkä komennon haluatte suorittaa?\n1: Uusi peli\n2: Lataa peli\n3: Poistu pelistä\nVastaus: ")

    if numerovalinta == "1":
        return numerovalinta, custom_nimet
    elif numerovalinta == "2":
        return numerovalinta, custom_nimet
    elif numerovalinta == "3":
        print ("\nMoro.")
        return numerovalinta, custom_nimet

# pelaajan_nimi = input("Mikä on nimenne?\nVastaus: ") # DEBUG - LAITA PÄÄLLE LOPULLISESSA VERSIOSSA
# pelaajan_ika = int(input("Mikä on ikänne?\nVastaus kokonaislukuna: ")) # DEBUG - LAITA PÄÄLLE LOPULLISESSA VERSIOSSA

import json
from esineet import Esine, Luettava
from huoneet import Huone, Tyhja
from mekanismit import Mekanismi, Este
from pelaaja import Pelaaja
pelaajan_nimi = ("Testeri") # DEBUG - LAITA POIS LOPULLISESSA VERSIOSSA
pelaajan_ika = 20 # DEBUG - LAITA POIS LOPULLISESSA VERSIOSSA

# -- Huoneet --
huone_2_3 = Huone("Käytävä", "auto", "auto", "auto", "auto")
huone_2_2 = Huone(f"Asunto, jonka omistaa {pelaajan_nimi}", huone_2_3, "auto", "auto", "auto")
for huone in Huone.lista_huoneista:
    huone.korjaa_huoneet()

# -- Esineet --
kartta = Luettava("Kartta", 0.2, (f"Kartassa lukee: 'Kartta on keskeneräinen. ASCII kartta tulossa, ehkä.'"))

# -- Mekanismit (eivät muutu tallennustiedoston mukaan, joten lisätään täällä) --
nappi = Este("Nappi", huone_2_2, False, True, True, True, True)
huone_2_2.lisaa_mekanismi(nappi)

if pelaajan_ika < 12:
    print ("\nOlette alaikäinen. Ette voi pelata.")
else:
    custom_nimet = ["Testeri2", "Testeri3", "Testeri4"] # DEBUG - LAITA POIS LOPULLISESSA VERSIOSSA
    numerovalinta, custom_nimet = paavalikko() # DEBUG - LAITA PÄÄLLE LOPULLISESSA VERSIOSSA
    if numerovalinta == "2":

        # -- Lataaminen --

        tallennuksen_nimi = input ("Kirjoita edellisen pelaajan nimi. Jos et muista, tarkista pelin tiedostoista '(nimi).json'-tiedosto. Isoilla kirjaimilla on väliä: ")
        with open (f"{tallennuksen_nimi}.json", "r") as tallennus:
            data_luettu = json.load(tallennus)
        pelaajan_nimi = data_luettu["pelaajan nimi"]
        pelaajan_ika = data_luettu["pelaajan ikä"]
        pelaajan_esineet = data_luettu["pelaajan esineet"]

        pelaajan_sijainti = data_luettu["pelaajan sijainti"]
        for huone in Huone.lista_huoneista:
            if huone.id == pelaajan_sijainti:
                pelaajan_sijainti = huone

        pelaaja = Pelaaja(pelaajan_nimi, pelaajan_sijainti)

        for esine_id in pelaajan_esineet:
            for esine in Esine.lista_esineista:
                if esine.id == esine_id:
                    pelaaja.lisaa_esine(esine)

        for huone in Huone.lista_huoneista:
            for esine_id in data_luettu[str(huone.id) + "esineet"]:
                for esine in Esine.lista_esineista:
                    if esine.id == esine_id:
                        huone.lisaa_esine(esine)
            # -- Ladataan esteet --
            huone.pohjoinen_estetty, huone.ita_estetty, huone.etela_estetty, huone.lansi_estetty = data_luettu[str(huone.id) + "esteet"]


        while pelaaja.valikko() != "0":
            if pelaaja.valikko() == "0":
                break

        # -- Tallentaminen --

        pelaaja_esineet_serialisoitu = []
        for esine in pelaaja.esineet:
            pelaaja_esineet_serialisoitu.append(esine.id)

        tallennus_data = {
            "pelaajan nimi": pelaajan_nimi,
            "pelaajan ikä": pelaajan_ika,
            "pelaajan esineet": pelaaja.serialisoi_esineet(),
            "pelaajan sijainti": pelaaja.sijainti.id,
        }

        for huone in Huone.lista_huoneista:
                tallennus_data[str(huone.id) + "esineet"] = huone.serialisoi_esineet()
                tallennus_data[str(huone.id) + "esteet"] = huone.serialisoi_esteet()
        
        with open (f"{pelaajan_nimi}.json", "w") as tallennus:
            json.dump(tallennus_data, tallennus)

    elif numerovalinta == "1":

        huone_2_2.lisaa_esine(kartta)
        pelaaja = Pelaaja(pelaajan_nimi, huone_2_2)
        
        while pelaaja.valikko() != "0":
            if pelaaja.valikko() == "0":
                break

        # -- Tallentaminen --
        # Mekanismien statusta ei vielä tallenneta. Ei riko peliä.

        pelaaja_esineet_serialisoitu = []
        for esine in pelaaja.esineet:
            pelaaja_esineet_serialisoitu.append(esine.id)

        tallennus_data = {
            "pelaajan nimi": pelaajan_nimi,
            "pelaajan ikä": pelaajan_ika,
            "pelaajan esineet": pelaaja.serialisoi_esineet(),
            "pelaajan sijainti": pelaaja.sijainti.id,
        }

        for huone in Huone.lista_huoneista:
                tallennus_data[str(huone.id) + "esineet"] = huone.serialisoi_esineet()
                tallennus_data[str(huone.id) + "esteet"] = huone.serialisoi_esteet()
        
        with open (f"{pelaajan_nimi}.json", "w") as tallennus:
            json.dump(tallennus_data, tallennus)