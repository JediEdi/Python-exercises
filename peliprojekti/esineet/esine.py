class Esine():
    def __init__(self, nimi, tilavuus):
        self.nimi = nimi
        self.tilavuus = tilavuus

    def kayta_esine(self):
        print (self.nimi)

class Luettava(Esine):
    def __init__(self, nimi, tilavuus, teksti):
        super().__init__(nimi, tilavuus)
        self.teksti = teksti

    def kayta_esine(self):
        print (self.teksti)

if __name__ == "__main__":
    testiesine = Luettava("Testi", 1, "Testi testi")
    testiesine.kayta_esine()