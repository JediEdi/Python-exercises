
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
huone_2_2 = Huone("Asunto", "auto" "auto", "auto", "auto", "asunnossanne", "Niin paljon huonekaluja, perheen muistoesineitä ja kodinkoneita... Mitään niistä ei voi juoda. Jatkakaa.")
huone_2_3 = Huone("Käytävä", "auto", "auto", huone_2_2, "auto", "asuntorakennuksen käytävässä", "Hmm. Ramin etuovi pohjoisessa on auki...")
huone_2_4 = Huone("Ramin asunto", "auto,", "auto", huone_2_3, "auto", "ramin asunnossa", "Asunto on tyhjä? Hän aina valitti köyhyyttään, mutta tämä tuli yllätyksenä. Hetkinen, lattialla on lappu...")
huone_3_3 = Huone("Eteinen", "auto", "auto", "auto", huone_2_3, "eteisessä", "Näissä etuoven asunnoissa kuulee varmaan jokaisen sisääntulijan. Siis kuuli.")
huone_3_4 = Huone("Irenen asunto", "auto", "auto", huone_3_3, "auto", "Irenen asunnossa", "Irene oli yksi ensimmäisistä, jotka lähtivät täältä. Itse ette pitäneet sitä hyökyaaltoa juuri minään. Ettekä vieläkään pidä.")

huone_4_3 = Huone("Katu", "auto", "auto", "auto", huone_3_3, "jalkakäytävällä", "Olittekin unohtanut, kuinka paksua ilma oli... Olisi pitänyt ainakin *harkita* sitä hybridiautoa.")
huone_5_3 = Huone("Presidentin huvila, ulko-ovi", "auto", "auto", "auto", huone_4_3, "presidentin huvilan ulko-ovella", "Nyt vain etsitään keino sisään.")
huone_5_4 = Huone("Presidentin huvila, pergola", "auto", "auto", huone_5_3, "auto", "presidentin huvilan pergolassa")
huone_6_4 = Huone("Presidentin huvila, heikko seinä", "auto", "auto", "auto", huone_5_4, "presidentin huvilan heikon seinän luona", "Katsos, kaivinkone. Juuri sopivasti!")

huone_5_2 = Huone("Presidentin huvila, puutarha", huone_5_3, "auto", "auto", "auto", "presidentin huvilan puutarhassa", "Ei ole kukkia. On vain levää... Jos mikään enää tuoksuisi, ette tiedä, tuoksuisiko tämä miljöö miltään.")

huone_u_0 = Huone("ei mitään?", "auto", huone_5_2, "auto", "auto", "maakuopan ympärillä", "Tuolla on jotain... Hypätkää alas. Ilma ottaa kopin.")
huone_u_1 = Huone("Tunnelin alku", Tyhja(), "auto", "auto", "auto", "tunnelin alussa", "Ette pääse enää takaisin. On pimeää. Seuratkaa ilmavirtaa.")

# maali = Huone("Presidentin huvila, KEITTIÖ", huone_6_4, Tyhja(), huone_6_2, "auto")

for huone in Huone.lista_huoneista:
    huone.korjaa_huoneet()

# -- Esineet --
kartta = Luettava("Kartta", 0.2, (f"Kartassa lukee: 'Kartta on keskeneräinen. ASCII kartta tulossa, ehkä.'"))
rami_lappu_1 = Luettava("Ramin lappu", 0.2, (f"Lapussa lukee: '{pelaajan_nimi}, minun lähdettyäni olet ainoa sielu koko kylässä.\nEn ole dorka; tiedän, että huomasit, kuinka varastin pressan huvilasta juomavettä kaikki nämä vuodet. Aion jättää tämän tiedon sinulle, hyvä ystäväni. Eksäni talossa on lisää tietoa. Ainoa nainen koko rakennuksessa.'"))
rami_lappu_2 = Luettava("Ramin lappu 2", 0.2, (f"Lapussa lukee: '{pelaajan_nimi}, pressan huvilaan on kolme reittiä. Ikkuna, seinästä läpi tai piilotettu, maanalainen tunneli. Ikkuna on rakennuksen eteläisessä seinässä, heikko muuraus pohjoisessa ja tunneli on kadun lähellä piilossa.'"))
irene_kirja = Luettava("Sensaatiolehti", 0.5, "Selaatte lehteä: 'VESI TAPPAA MEIDÄT KAIKKI! * alan huipputieteilijät ovat ennustaneet, että vuoteen 2600 mennessä ihmiskunta saa kärsiä historian rankimman hyökyaallon. Katukaa syntejänne ja tilatkaa SENSAATIOLEHTI PLUS, ja me ehkä selviämme!!!       * Astrologian'")
lore_dump = Luettava("Ramin lappu 0", 0.2, "Lapussa lukee: 'Niin se sitten meni. Hyökyaalto saapui, ja nousi nousemistaan. Jos satelliitit toimisivat enää, näkymä olisi aaaika kiinnostava. Itse olen ainakin samaa mieltä niiden astrologien kanssa, että nyt, kun vettä on hirveän paljon ja ilmaa niin vähän, voitaisiin vaihtaa niiden nimet. Nyt me hengitämme vettä ja juomme ilmaa. Onneksi kävin sillä kesäleirillä. Opinpa sukeltamaan!'")
tikkaat = Esine("Tikkaat", 10)

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

        # Uusi peli alkaa. Alustetaan se asettamalla kaikki paikoilleen. Tekisi mieli ladata tämäkin vain .json-tiedostosta, mutta ei jaksa.

        huone_2_2.lisaa_esine(kartta)
        huone_2_4.lisaa_esine(rami_lappu_1)
        huone_3_4.lisaa_esine(rami_lappu_2)
        huone_3_4.lisaa_esine(irene_kirja)
        huone_u_1.lisaa_esine(lore_dump)
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