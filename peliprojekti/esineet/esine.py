class Esine():
    lista_esineista = []
    def __init__(self, nimi, tilavuus):
        self.nimi = nimi
        self.tilavuus = tilavuus
        self.id = len(Esine.lista_esineista)
        Esine.lista_esineista.append(self)

    def kayta_esine(self):
        print (self.nimi)

    # def serialisoi(self):
    #     return (f"{self.nimi}\n{self.tilavuus}")

class Luettava(Esine):
    def __init__(self, nimi, tilavuus, teksti):
        super().__init__(nimi, tilavuus)
        self.teksti = teksti

    def kayta_esine(self):
        print (self.teksti)

    # def serialisoi(self):
    #     return (f"{self.nimi} {self.tilavuus}\n{self.teksti}")
        

if __name__ == "__main__":
    testiesine = Luettava("Testi", 1, "Testi testi")
    testiesine.kayta_esine()