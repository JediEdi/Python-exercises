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
            elif self.sijainti.pohjoinen_estetty == True:
                print ("Reitillä pohjoiseen on este!")
            else:
                self.sijainti = self.sijainti.pohjoisessa
        if suunta == "I":
            if self.sijainti.idassa.nimi == "ei mitään":
                print ("Idässä ei ole mitään.")
            elif self.sijainti.ita_estetty == True:
                print ("Reitillä itään on este!")
            else:
                self.sijainti = self.sijainti.idassa
        if suunta == "E":
            if self.sijainti.etelassa.nimi == "ei mitään":
                print ("Etelässä ei ole mitään.")
            elif self.sijainti.etela_estetty == True:
                print ("Reitillä etelään on este!")
            else:
                self.sijainti = self.sijainti.etelassa
        if suunta == "L":
            if self.sijainti.lannessa.nimi == "ei mitään":
                print ("Lännessä ei ole mitään.")
            elif self.sijainti.lansi_estetty == True:
                print ("Reitillä länteen on este!")
            else:
                self.sijainti = self.sijainti.lannessa

    def katso_ymparille(self):
        numero = 0
        print (f"\nOlette {self.sijainti.prepositio}.")
        if self.sijainti.kuvaus != "":
            print (self.sijainti.kuvaus)
        if self.sijainti.pohjoinen_estetty == True:
            print ("\nPohjoiseen on pääsy estetty.")
        if self.sijainti.ita_estetty == True:
            print ("Itään on pääsy estetty.")
        if self.sijainti.etela_estetty == True:
            print ("Etelään on pääsy estetty.")
        if self.sijainti.lansi_estetty == True:
            print ("Länteen on pääsy estetty.")
        print (f"\n{self.sijainti.prepositio} on seuraavat esineet:")
        for esine in self.sijainti.esineet:
            numero += 1
            print (f"{numero}: {esine.nimi}")

        numero = 0
        print (f"\n{self.sijainti.prepositio} on seuraavat mekanismit:")
        for mekanismi in self.sijainti.mekanismit:
            numero += 1
            print (f"{numero}: {mekanismi.nimi}")
        print (f"\nPohjoisessa on {self.sijainti.pohjoisessa.nimi}. Idässä on {self.sijainti.idassa.nimi}. Etelässä on {self.sijainti.etelassa.nimi}. Lännessä on {self.sijainti.lannessa.nimi}.")

    def kayta_esine(self, esine_numero):
        esine_numero -= 1
        if esine_numero < len(self.esineet):
            print (f"Käytitte seuraavan esineeen: {self.esineet[esine_numero].nimi}.")
            self.esineet[esine_numero].kayta_esine()


    def lisaa_esine(self, esine):
        self.esineet.append(esine)
        print (f"Saitte seuraavan esineeen: {esine.nimi}.")

    def luettele_esineet(self):
        numero = 0
        print ("\nTeillä on seuraavat esineet:")
        for esine in self.esineet:
            numero += 1
            print (f"{numero}: {esine.nimi}")

    # def serialisoi_esineet(self):
    #     self.esineet_serialisoitu = []
    #     for esine in self.esineet:
    #         self.esineet_serialisoitu.append(esine.id)
    #     return self.esineet_serialisoitu


    def valikko(self):
        print (f"\nLista mahdollisista toiminnoista:\n1. Liiku\n2. Katso ympärille\n3. Käytä esine tavaraluettelossa\n4. Nouki esine ympäristöstä\n5. Vuorovaikuta mekanismin kanssa\n0. Poistu")
        numerovalinta = input("Mitä haluatte tehdä? Vastaus numerona: ")
        if numerovalinta == "1":
            suuntavalinta = input("Mihin suuntaan haluatte liikkua? Vastaus [P (pohjoinen), I (itä), E (etelä), L (länsi)]: ")
            self.liiku(suuntavalinta)
        elif numerovalinta == "2":
            self.katso_ymparille()
        elif numerovalinta == "3":
            self.luettele_esineet()
            esinevalinta = int(input("Minkä esineen haluatte käyttää? Vastaus numerona: "))
            self.kayta_esine(esinevalinta)
        elif numerovalinta == "4":
            esinevalinta = int(input("Minkä esineen haluatte noukkia? Vastaus numerona: ")) - 1
            if esinevalinta < len(self.sijainti.esineet):
                self.lisaa_esine(self.sijainti.esineet[esinevalinta])
                self.sijainti.esineet.pop(esinevalinta)
        elif numerovalinta == "5":
            mekanismivalinta = int(input("Minkä mekanismin kanssa haluatte vuorovaikuttaa? Vastaus numerona: ")) - 1
            if mekanismivalinta < len(self.sijainti.mekanismit):
                self.sijainti.mekanismit[mekanismivalinta].kayta_mekanismi()
        elif numerovalinta == "0":
            return "0"