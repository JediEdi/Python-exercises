class Pelaaja():
    def __init__(self, nimi, sijainti):
        self.nimi = nimi
        self.esineet = []
        self.sijainti = sijainti

    def liiku(self, suunta):
        self.suunta = suunta
        if suunta == "N":
            if self.sijainti.pohjoisessa.nimi == "Ei mitään":
                print ("Pohjoisessa ei ole mitään.")
            else:
                self.sijainti = self.sijainti.pohjoisessa

    def katso_ymparille(self):
        print (f"\nOlet huoneessa nimeltään {self.sijainti.nimi}.")
        print ("\nHuoneessa on seuraavat esineet:")
        for esine in self.sijainti.esineet:
            print (esine.nimi)
        print ("\nHuoneessa on seuraavat mekanismit:")
        for mekanismi in self.sijainti.mekanismit:
            print (mekanismi.nimi)
        print (f"\nPohjoisessa on {self.sijainti.pohjoisessa.nimi}. Idässä on {self.sijainti.idassa.nimi}. Etelässä on {self.sijainti.etelassa.nimi}. Lännessä on {self.sijainti.lannessa.nimi}.")

    def kayta_esine(self, esine_numero):
        self.esineet[esine_numero].kayta_esine

    def lisaa_esine(self, esine):
        self.esineet.append(esine)

    def luettele_esineet(self):
        for esine in self.esineet:
            print (esine.nimi)