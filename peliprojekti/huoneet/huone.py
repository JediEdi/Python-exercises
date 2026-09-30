class Huone():
    def __init__(self, nimi, pohjoisessa, idassa, etelassa, lannessa):
        self.nimi = nimi
        self.pohjoisessa = pohjoisessa
        self.idassa = idassa
        self.etelassa = etelassa
        self.lannessa = lannessa
        self.esineet = []
        self.mekanismit = []

    def lisaa_esine(self, esine):
        self.esineet.append(esine)
        return

    def lisaa_mekanismi(self, mekanismi):
        self.mekanismit.append(mekanismi)
        return

    def luettele_esineet(self):
        for esine in self.esineet:
            print (esine.nimi)

class Tyhja(Huone):
    def __init__(self, nimi = "ei mitään"):
        self.nimi = nimi
