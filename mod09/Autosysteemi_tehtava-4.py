import random

class Auto:

    autojen_maara = 0

    def __init__(self, rekisteritunnus, huippunopeus, hetkellinen_nopeus = 0, kuljettu_matka = 0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.hetkellinen_nopeus = hetkellinen_nopeus
        self.kuljettu_matka = kuljettu_matka
        Auto.autojen_maara = Auto.autojen_maara + 1

    def kiihdytä(self, nopeuden_muutos):
        self.hetkellinen_nopeus = (self.hetkellinen_nopeus + nopeuden_muutos)
        if (self.hetkellinen_nopeus > self.huippunopeus):
            self.hetkellinen_nopeus = self.huippunopeus
        elif (self.hetkellinen_nopeus < 0):
            self.hetkellinen_nopeus = 0

    def kulje(self, tuntimaara):
        self.kuljettu_matka = (self.kuljettu_matka + (tuntimaara * self.hetkellinen_nopeus))
        return self.kuljettu_matka

kilpailijat = []
for kilpailija in range(10):
    auto = Auto("ABC" + str(Auto.autojen_maara + 1), random.randint(100, 200)) # Python osaa näköjään määrittää uniikit nimet luoduille objecteille. Riippuu sijainnista välimuistissa?
    print (f"Auto {auto.rekisteritunnus}: Huippunopeus on: {auto.huippunopeus}")
    kilpailijat.append (auto)

voittaja_valittu = 0

while voittaja_valittu == 0:
    for auto in kilpailijat:
            auto.kiihdytä(random.randint(-10, 15))
            auto.kulje(1)
            if auto.kuljettu_matka >= 10000:
                voittaja_valittu = 1
                print ("\nAuto, jonka rekisteritunnus on " + auto.rekisteritunnus + " on ylittänyt maaliviivan ensimmäisenä!")

for auto in kilpailijat:
    print ("Rekisteritunnus: " + auto.rekisteritunnus + " | Huippunopeus: " + str(auto.huippunopeus) + " | Hetkellinen nopeus: " + str(auto.hetkellinen_nopeus) + " | Kuljettu matka: " + str(auto.kuljettu_matka))