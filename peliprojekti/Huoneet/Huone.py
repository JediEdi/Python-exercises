class Huone():
    def __init__(self, nimi):
        self.nimi = nimi
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