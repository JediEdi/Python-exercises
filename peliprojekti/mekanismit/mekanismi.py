class Mekanismi():
    def __init__(self, nimi):
        self.nimi = nimi

    def kayta_esineella(self, pelaaja, esine):
        if esine in pelaaja.esineet:
            print (f"Käytit mekanismin {self.nimi}!")