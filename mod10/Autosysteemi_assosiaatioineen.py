import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, hetkellinen_nopeus = 0, kuljettu_matka = 0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.hetkellinen_nopeus = hetkellinen_nopeus
        self.kuljettu_matka = kuljettu_matka

    def kiihdytä(self, nopeuden_muutos):
        self.hetkellinen_nopeus = (self.hetkellinen_nopeus + nopeuden_muutos)
        if (self.hetkellinen_nopeus > self.huippunopeus):
            self.hetkellinen_nopeus = self.huippunopeus
        elif (self.hetkellinen_nopeus < 0):
            self.hetkellinen_nopeus = 0

    def kulje(self, tuntimaara):
        self.kuljettu_matka = (self.kuljettu_matka + (tuntimaara * self.hetkellinen_nopeus))
        return self.kuljettu_matka

class Kilpailu:
    def __init__(self, nimi, pituus, kilpailijoiden_lukumaara, tunteja_kulunut = 0):
        self.nimi = nimi
        self.pituus = pituus
        self.kilpailijoiden_lukumaara = kilpailijoiden_lukumaara
        self.kilpailijat = []
        for kilpailija in range(kilpailijoiden_lukumaara):
            auto = Auto("ABC" + str(self.kilpailijat.__len__() + 1), random.randint(100, 200))
            print (f"Auto {auto.rekisteritunnus}: Huippunopeus on: {auto.huippunopeus}")
            self.kilpailijat.append (auto)
        self.tunteja_kulunut = tunteja_kulunut

    def tunti_kuluu(self):
        for auto in self.kilpailijat:
            auto.kiihdytä(random.randint(-10, 15))
            auto.kulje(1)

    def tulosta_tilanne(self):
        print ("\nTulokset:")
        for auto in self.kilpailijat:
            print ("Rekisteritunnus: " + auto.rekisteritunnus + " | Huippunopeus: " + str(auto.huippunopeus) + " | Hetkellinen nopeus: " + str(auto.hetkellinen_nopeus) + " | Kuljettu matka: " + str(auto.kuljettu_matka))

    def kilpailu_ohi(self):
        kilpailu_ohi = False
        while kilpailu_ohi == False:
            for auto in self.kilpailijat:
                if auto.kuljettu_matka >= self.pituus:
                    print ("\nAuto, jonka rekisteritunnus on " + auto.rekisteritunnus + " on ylittänyt maaliviivan ensimmäisenä!")
                    kilpailu_ohi = True
                    return kilpailu_ohi
                else:
                    return kilpailu_ohi


romuralli = Kilpailu("Suuri romuralli", 8000, 10)

while romuralli.kilpailu_ohi() == False:
    romuralli.tunti_kuluu()
    romuralli.tunteja_kulunut = romuralli.tunteja_kulunut + 1
    if romuralli.tunteja_kulunut % 10 == 0:
        romuralli.tulosta_tilanne()
romuralli.tulosta_tilanne()