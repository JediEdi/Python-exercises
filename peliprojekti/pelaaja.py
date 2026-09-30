class Pelaaja():
    def __init__(self, nimi, sijainti):
        self.nimi = nimi
        self.esineet = []
        self.sijainti = sijainti

    def liiku(self, suunta):
        self.suunta = suunta
        if suunta == "P":
            if self.sijainti.pohjoisessa.nimi == "ei mitään":
                print ("Pohjoisessa ei ole mitään.")
            else:
                self.sijainti = self.sijainti.pohjoisessa
        if suunta == "I":
            if self.sijainti.idassa.nimi == "ei mitään":
                print ("Idässä ei ole mitään.")
            else:
                self.sijainti = self.sijainti.idassa
        if suunta == "E":
            if self.sijainti.etelassa.nimi == "ei mitään":
                print ("Etelässä ei ole mitään.")
            else:
                self.sijainti = self.sijainti.etelassa
        if suunta == "L":
            if self.sijainti.lannessa.nimi == "ei mitään":
                print ("Lännessä ei ole mitään.")
            else:
                self.sijainti = self.sijainti.lannessa

    def katso_ymparille(self):
        print (f"\nOlette huoneessa nimeltään {self.sijainti.nimi}.")
        print ("\nHuoneessa on seuraavat esineet:")
        for esine in self.sijainti.esineet:
            print (esine.nimi)
        print ("\nHuoneessa on seuraavat mekanismit:")
        for mekanismi in self.sijainti.mekanismit:
            print (mekanismi.nimi)
        print (f"\nPohjoisessa on {self.sijainti.pohjoisessa.nimi}. Idässä on {self.sijainti.idassa.nimi}. Etelässä on {self.sijainti.etelassa.nimi}. Lännessä on {self.sijainti.lannessa.nimi}.")

    def kayta_esine(self, esine_numero):
        esine_numero -= 1
        print (f"Käytitte seuraavan esineeen: {self.esineet[esine_numero].nimi}.")
        self.esineet[esine_numero].kayta_esine()


    def lisaa_esine(self, esine):
        self.esineet.append(esine)
        print (f"Saitte seuraavan esineeen: {esine}.")

    def luettele_esineet(self):
        numero = 0
        print ("\nTeillä on seuraavat esineet:")
        for esine in self.esineet:
            numero += 1
            print (f"{numero}: {esine.nimi}")