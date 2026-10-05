class Huone():
    lista_huoneista = []
    def __init__(self, nimi, pohjoisessa, idassa, etelassa, lannessa, pohjoinen_estetty = False, ita_estetty = False, etela_estetty = False, lansi_estetty = False):
        self.nimi = nimi
        self.pohjoisessa = pohjoisessa
        self.idassa = idassa
        self.etelassa = etelassa
        self.lannessa = lannessa
        self.pohjoinen_estetty = pohjoinen_estetty
        self.ita_estetty = ita_estetty
        self.etela_estetty = etela_estetty
        self.lansi_estetty = lansi_estetty
        self.esineet = []
        self.mekanismit = []
        self.id = len(Huone.lista_huoneista)
        Huone.lista_huoneista.append(self)

    def korjaa_huoneet(self):
        if self.pohjoisessa == "auto":
            for huone in Huone.lista_huoneista:
                if huone.etelassa == self:
                    self.pohjoisessa = huone
                else:
                    self.pohjoisessa = Tyhja()

        if self.idassa == "auto":
            for huone in Huone.lista_huoneista:
                if huone.lannessa == self:
                    self.idassa = huone
                else:
                    self.idassa = Tyhja()

        if self.etelassa == "auto":
            for huone in Huone.lista_huoneista:
                if huone.pohjoisessa == self:
                    self.etelassa = huone
                else:
                    self.etelassa = Tyhja()

        if self.lannessa == "auto":
            for huone in Huone.lista_huoneista:
                if huone.idassa == self:
                    self.lannessa = huone
                else:
                    self.lannessa = Tyhja()


    def lisaa_esine(self, esine):
        self.esineet.append(esine)
        return

    def lisaa_mekanismi(self, mekanismi):
        self.mekanismit.append(mekanismi)
        return

    def luettele_esineet(self):
        for esine in self.esineet:
            print (esine.nimi)

    def serialisoi_esineet(self):
        self.esineet_serialisoitu = []
        for esine in self.esineet:
            self.esineet_serialisoitu.append(esine.id)
        return self.esineet_serialisoitu

    def serialisoi_esteet(self):
        self.esteet_serialisoitu = [self.pohjoinen_estetty, self.ita_estetty, self.etela_estetty, self.lansi_estetty]
        return self.esteet_serialisoitu

class Tyhja(Huone):
    def __init__(self, nimi = "ei mitään"):
        self.nimi = nimi
