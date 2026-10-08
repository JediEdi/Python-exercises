class Esine():
    lista_esineista = []
    def __init__(self, nimi, tilavuus, toimintokuvaus = "Käytitte esineen.", printtaaja = False):
        self.nimi = nimi
        self.tilavuus = tilavuus
        self.toimintokuvaus = toimintokuvaus
        self.printtaaja = printtaaja
        self.id = len(Esine.lista_esineista)
        Esine.lista_esineista.append(self)

    def kayta_esine(self):
        print (self.toimintokuvaus)
        # Jos peli olisi suurempi, tekisin tänne jotain presettejä.



class Luettava(Esine):
    def __init__(self, nimi, tilavuus, teksti, printtaaja = False):
        super().__init__(nimi, tilavuus, toimintokuvaus = "Käytitte esineen.")
        self.teksti = teksti
        self.printtaaja = printtaaja # Esine käytetääb, siis luetaan heti, kun sen noukkii.

    def kayta_esine(self):
        print (self.teksti)