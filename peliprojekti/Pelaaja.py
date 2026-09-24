class Pelaaja():
    def __init__(self, nimi, sijainti):
        self.nimi = nimi
        self.esineet = []
        self.sijainti = sijainti

    def liiku(self, suunta):
        self.suunta = suunta

    def kayta_esine(self, esine_numero):
        self.esineet[esine_numero].kayta_esine

    def lisaa_esine(self, esine):
        self.esineet.append(esine)

    def luettele_esineet(self):
        for esine in self.esineet:
            print (esine.nimi)