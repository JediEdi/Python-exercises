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

auto = Auto("ABC-123", 142)
print ("Rekisteritunnus: " + auto.rekisteritunnus)
print ("Huippunopeus: " + str(auto.huippunopeus) + " km/h")
print ("Hetkellinen nopeus: " + str(auto.hetkellinen_nopeus) + " km/h")
print ("Kuljettu matka: " + str(auto.kuljettu_matka))

auto.kiihdytä(30)
auto.kulje(1)
print ("\nHetkellinen nopeus: " + str(auto.hetkellinen_nopeus) + " km/h")
print ("Kuljettu matka: " + str(auto.kuljettu_matka) + "km")
auto.kiihdytä(70)
auto.kulje(1)
print ("Hetkellinen nopeus: " + str(auto.hetkellinen_nopeus) + " km/h")
print ("Kuljettu matka: " + str(auto.kuljettu_matka) + "km")
auto.kiihdytä(50)
auto.kulje(1)
print ("Hetkellinen nopeus: " + str(auto.hetkellinen_nopeus) + " km/h")
print ("Kuljettu matka: " + str(auto.kuljettu_matka) + "km")
auto.kiihdytä(-200)
auto.kulje(1)
print ("Hetkellinen nopeus: " + str(auto.hetkellinen_nopeus) + " km/h")
print ("Kuljettu matka: " + str(auto.kuljettu_matka) + "km")

