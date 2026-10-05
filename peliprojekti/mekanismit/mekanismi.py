class Mekanismi():
    def __init__(self, nimi):
        self.nimi = nimi

    def kayta_mekanismi(self):
        print (f"Käytit mekanismin {self.nimi}.")

    def kayta_esineella(self, pelaaja, esine):
        if esine in pelaaja.esineet:
            print (f"Käytit mekanismin {self.nimi}.")

class Este(Mekanismi):
    def __init__(self, nimi, vaikutusalue, kertakayttoinen = False, esta_pohjoinen = False, esta_ita = False, esta_etela = False, esta_lansi = False):
        super().__init__(nimi)
        self.vaikutusalue = vaikutusalue
        self.kertakayttoinen = kertakayttoinen
        self.esta_pohjoinen = esta_pohjoinen
        self.esta_ita = esta_ita
        self.esta_etela = esta_etela
        self.esta_lansi = esta_lansi
        self.mekanismi_vaihe = True # Jos False, vaikutus on päinvastainen. Pohjoisen sulkeminen olisi nyt pohjoisen avaaminen.
        self.mekanismi_kaytettava = True

    def kayta_mekanismi(self):
        if self.mekanismi_kaytettava == False:
            print (f"Mekanismia {self.nimi} ei voi käyttää!")
        else:
            if self.mekanismi_vaihe == True:
                print (f"Mekanismi {self.nimi} käytettiin.")
                self.vaikutusalue.pohjoinen_estetty = self.esta_pohjoinen
                print (f"Pohjoinen estetty: {self.vaikutusalue.pohjoinen_estetty}!")
                self.vaikutusalue.ita_estetty = self.esta_ita
                print (f"Itä estetty: {self.vaikutusalue.ita_estetty}!")
                self.vaikutusalue.etela_estetty = self.esta_etela
                print (f"Etelä estetty: {self.vaikutusalue.etela_estetty}!")
                self.vaikutusalue.lansi_estetty = self.esta_lansi
                print (f"Länsi estetty: {self.vaikutusalue.lansi_estetty}!")
                if self.kertakayttoinen == True:
                    self.mekanismi_kaytettava = False
                    print (f"Mekanismi {self.nimi} lukkiutuu!")
                self.mekanismi_vaihe = False
            
            else:
                print (f"Mekanismi {self.nimi} käytettiin taas.")
                self.vaikutusalue.pohjoinen_estetty = not self.esta_pohjoinen
                print (f"Pohjoinen estetty: {self.vaikutusalue.pohjoinen_estetty}!")
                self.vaikutusalue.ita_estetty = not self.esta_ita
                print (f"Itä estetty: {self.vaikutusalue.ita_estetty}!")
                self.vaikutusalue.etela_estetty = not self.esta_etela
                print (f"Etelä estetty: {self.vaikutusalue.etela_estetty}!")
                self.vaikutusalue.lansi_estetty = not self.esta_lansi
                print (f"Länsi estetty: {self.vaikutusalue.lansi_estetty}!")
                self.mekanismi_vaihe = True