class Esine():
    lista_esineista = []
    def __init__(self, nimi, tilavuus, toimintokuvaus = "Käytitte esineen.", printtaaja = False):
        self.nimi = nimi
        self.tilavuus = tilavuus
        self.toimintokuvaus = toimintokuvaus
        self.printtaaja = printtaaja # Esine käytetään heti, kun sen noukkii. Tämä toiminto on pelaaja-luokan sisällä. Tässä tapauksessa Graalin malja vain printtaa konsoliin.
        self.id = len(Esine.lista_esineista) # Käytetään tallentamiseen ja lataamiseen.
        Esine.lista_esineista.append(self)

    def kayta_esine(self):
        print (self.toimintokuvaus)
        # Jos peli olisi suurempi, tekisin tänne jotain presettejä.



class Luettava(Esine):
    def __init__(self, nimi, tilavuus, teksti, printtaaja = False):
        super().__init__(nimi, tilavuus, toimintokuvaus = "Käytitte esineen.")
        self.teksti = teksti
        self.printtaaja = printtaaja

    def kayta_esine(self):
        print (self.teksti)