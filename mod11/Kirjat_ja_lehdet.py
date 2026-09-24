class Julkaisu():
    def __init__(self, nimi):
        self.nimi = nimi

    def tulosta_tiedot(self):
        print ("Nimi: " + self.nimi)

class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumaara):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print ("Kirjan kirjoittaja: " + self.kirjoittaja)
        print ("Kirjan sivumäärä: " + str(self.sivumaara))

class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        super().__init__(nimi)
        self.paatoimittaja = paatoimittaja

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print ("Lehden päätoimittaja: " + self.paatoimittaja)


aku_ankka = Lehti("Aku Ankka", "Aki Hyyppä")
hytti = Kirja("Hytti nro. 6", "Rosa Liksom", 200)

aku_ankka.tulosta_tiedot()
hytti.tulosta_tiedot()