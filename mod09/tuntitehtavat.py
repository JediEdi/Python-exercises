# 1: Pelihahmo
# class Pelaaja:
#     def __init__(self, nimi, elamat = 3, kolikot = 0, pisteet = 0):
#         self.nimi = nimi
#         self.elamat = elamat
#         self.kolikot = kolikot
#         self.pisteet = pisteet

# mario = Pelaaja("Mario")
# print ("Marion elämät: " + str(mario.elamat))
# print ("Marion kolikot: " + str(mario.kolikot))
# print ("Marion pisteet: " + str(mario.pisteet))

# 2: Piraatti ARRR!
# class Merirosvolaiva:
#     def __init__(self, nimi, tykkien_maara, miehiston_maara, kulta = 0):
#         self.nimi = nimi
#         self.tykkien_maara = tykkien_maara
#         self.miehiston_maara = miehiston_maara
#         self.kulta = kulta

#     def loyda_aarre(self, maara):
#         self.kulta = self.kulta + maara

#     def meneta_aarre(self, maara):
#         self.kulta = self.kulta - maara
#         if self.kulta < 0:
#             self.kulta = 0

#     def palkkaa_miehistoa(self, maara):
#         self.miehiston_maara = self.miehiston_maara + maara

# black_pearl = Merirosvolaiva("The Black Pearl", 12, 40)

# black_pearl.loyda_aarre(200)
# black_pearl.loyda_aarre(75)
# black_pearl.meneta_aarre(100)
# black_pearl.palkkaa_miehistoa(3)

# print (f"{black_pearl.nimi} {black_pearl.tykkien_maara} {black_pearl.miehiston_maara} {black_pearl.kulta}")

# 3: Mario Kart
import random

class Auto:

    autojen_maara = 0

    def __init__(self, nimi, huippunopeus, hetkellinen_nopeus = 0, kuljettu_matka = 0):
        self.nimi = nimi
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

mario = Auto("Mario", random.randint(100, 180))
print (f"Hahmon {mario.nimi}: Huippunopeus on: {mario.huippunopeus}")
kilpailijat.append (mario)

luigi = Auto("Weegee", random.randint(100, 180))
print (f"Hahmon {luigi.nimi}: Huippunopeus on: {luigi.huippunopeus}")
kilpailijat.append (luigi)


peach = Auto("Peach", random.randint(100, 180))
print (f"Hahmon {peach.nimi}: Huippunopeus on: {peach.huippunopeus}")
kilpailijat.append (peach)


toad = Auto("Toad", random.randint(100, 180))
print (f"Hahmon {toad.nimi}: Huippunopeus on: {toad.huippunopeus}")
kilpailijat.append (toad)


bowser = Auto("Bowser", random.randint(100, 180))
print (f"Hahmon {bowser.nimi}: Huippunopeus on: {bowser.huippunopeus}")
kilpailijat.append (bowser)


yoshi = Auto("Yoshi", random.randint(100, 180))
print (f"Hahmon {yoshi.nimi}: Huippunopeus on: {yoshi.huippunopeus}")
kilpailijat.append (yoshi)


voittaja_valittu = 0

while voittaja_valittu == 0:
    for auto in kilpailijat:
            auto.kiihdytä(random.randint(-15, 30))
            auto.kulje(1)
            if auto.kuljettu_matka >= 1000:
                voittaja_valittu = 1
                print ("\nAuto, jonka nimi on " + auto.nimi + " on ylittänyt maaliviivan ensimmäisenä!")

for auto in kilpailijat:
    print ("nimi: " + auto.nimi + " | Huippunopeus: " + str(auto.huippunopeus) + " | Hetkellinen nopeus: " + str(auto.hetkellinen_nopeus) + " | Kuljettu matka: " + str(auto.kuljettu_matka))