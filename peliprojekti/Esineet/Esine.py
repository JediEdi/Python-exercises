class Esine():
    def __init__(self, nimi, tilavuus):
        self.nimi = nimi
        self.tilavuus = tilavuus

class Luettava(Esine):
    def __init__(self, nimi, tilavuus, teksti):
        super().__init__(nimi, tilavuus)
        self.teksti = teksti

    def kayta_esine(self):
        print (self.teksti)