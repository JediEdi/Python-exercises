class Mekanismi():
    def __init__(self, nimi):
        self.nimi = nimi

    def kayta_mekanismi(self):
        print (f"Käytitte mekanismin {self.nimi}.")

    def kayta_esineella(self, pelaaja, esine):
        if esine in pelaaja.esineet:
            print (f"Käytitte mekanismin {self.nimi}.")

class Este(Mekanismi):
    def __init__(self, nimi, vaikutusalue, toimintokuvaus = ("Käytitte mekanismin."), kertakayttoinen = False, esta_pohjoinen = False, esta_ita = False, esta_etela = False, esta_lansi = False, vaadittu_esine = "auto"):
        super().__init__(nimi)
        self.vaikutusalue = vaikutusalue
        self.toimintokuvaus = toimintokuvaus
        self.kertakayttoinen = kertakayttoinen
        self.esta_pohjoinen = esta_pohjoinen
        self.esta_ita = esta_ita
        self.esta_etela = esta_etela
        self.esta_lansi = esta_lansi
        self.vaadittu_esine = vaadittu_esine
        self.mekanismi_vaihe = True # Jos False, vaikutus on päinvastainen. Pohjoisen sulkeminen olisi nyt pohjoisen avaaminen.
        self.mekanismi_kaytettava = True

    def kayta_mekanismi(self, pelaaja): # Jos haluaa huoneeseen estetyn suunnan pelin alusta asti, tämä pitää tehdä huonetta luodessa.
        if self.mekanismi_kaytettava == False:
            print (f"Mekanismia {self.nimi} ei voi käyttää!")
        elif self.vaadittu_esine != "auto" and self.vaadittu_esine not in pelaaja.esineet:
                print (f"Mekanismi {self.nimi} vaatii esineen, jota teillä ei ole.")
        else:
            if self.mekanismi_vaihe == True:
                print (self.toimintokuvaus)
                if self.esta_pohjoinen == True or self.esta_pohjoinen == False: # Esim. jos kirjoittaa "auto", mikään ei muutu käytettäessä mekanismia.
                    self.vaikutusalue.pohjoinen_estetty = self.esta_pohjoinen
                    print (f"Pohjoinen estetty: {self.vaikutusalue.pohjoinen_estetty}!")
                if self.esta_ita == True or self.esta_ita == False:
                    self.vaikutusalue.ita_estetty = self.esta_ita
                    print (f"Itä estetty: {self.vaikutusalue.ita_estetty}!")
                if self.esta_etela == True or self.esta_etela == False:
                    self.vaikutusalue.etela_estetty = self.esta_etela
                    print (f"Etelä estetty: {self.vaikutusalue.etela_estetty}!")
                if self.esta_lansi == True or self.esta_lansi == False:
                    self.vaikutusalue.lansi_estetty = self.esta_lansi
                    print (f"Länsi estetty: {self.vaikutusalue.lansi_estetty}!")
                if self.kertakayttoinen == True:
                    self.mekanismi_kaytettava = False
                    print (f"Mekanismi {self.nimi} ei ole enää käytettävissä.")
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

class Kaivinkone(Este): # Ei ole idyllinen käyttö luokalle, mutta on kiire.
    def __init__(self, nimi, vaikutusalue, toimintokuvaus="\nOlette kaivinkoneessa.", kertakayttoinen=True, esta_pohjoinen="auto", esta_ita="auto", esta_etela=False, esta_lansi="auto", vaadittu_esine="auto"):
        super().__init__(nimi, vaikutusalue, toimintokuvaus, kertakayttoinen, esta_pohjoinen, esta_ita, esta_etela, esta_lansi, vaadittu_esine)

    def kayta_mekanismi(self, pelaaja):
        print (self.toimintokuvaus)
        if self.vaikutusalue.etela_estetty == False:
            print ("Seinä on jo murrettu.")
        else:
            virta = False
            suunta = "pohjoiseen"
            etaisyys = 3
            seina_hp = 2
            kasijarru = False
            kytkin = False

            while seina_hp > 0:
                print ("Edessänne on viisi kahvaa, kolme poljinta ja kaksi nappia. Missään ei ole ohjeita. Avain on jo koneessa, mutta kone ei ole käynnissä.")
                numerovalinta = input("Mitä haluatte tehdä?\n1: Kahva vasemmalla\n2: Kahva edessänne\n3: Kahva etuoikealla\n4: Kahva keskioikealla\n5: Kahva oikealla\n6: Poljin vasemmalla\n7: Poljin keskellä\n8: Poljin oikealla\n9: Nappi edessänne\n10: Nappi vieressänne\n0: POIS TÄÄLTÄ\nVastaus numerona: ")
                if numerovalinta != "9" and numerovalinta != "4" and numerovalinta != "7":
                    if virta == False:
                        print ("Mitään ei tapahdu.")
                elif numerovalinta == "1":
                    print ("Koura liikkuu ulommas.")
                    if suunta == "etelään" and etaisyys == 2:
                        if seina_hp == 2:
                            print ("Koura törmää seinään ja jättää jälkeensä tuhoa, sirpaleita ja murtumia. Seinä on kuitenkin yhä tolpillaan. Tee se uudelleen.")
                            seina_hp = 1
                        elif seina_hp == 1:
                            print ("Tällä kertaa koura leikkaa suoraan seinän läpi. Tunnette hytissä tärähdyksiä vielä useita sekunteja osuman jälkeen. Seinä on murskattu.")
                            seina_hp = 0
                    elif suunta == "etelään" and etaisyys < 2:
                        print ("Kouralla ei ole tilaa kerätä voimaa. Se tömähtää seinään heikosti. Seinälle ei käy kuinkaan.")
                elif numerovalinta == "2":
                    if suunta == "pohjoiseen":
                        suunta = "itään"
                    elif suunta == "itään":
                        suunta = "etelään"
                    elif suunta == "etelään":
                        suunta = "länteen"
                    elif suunta == "länteen":
                        suunta = "pohjoiseen"
                    print (f"Kaivinkone pyörii myötäpäivään. Se osoittaa nyt {suunta}.")
                elif numerovalinta == "3":
                    print ("Koura liikkuu vaakasuorassa, mutta todella vähän. Huoltoryhmä on mokannut.")
                elif numerovalinta == "4":
                    if kasijarru == False:
                        print ("Kahva jäi asentoonsa. Kaivinkone nytkähti hieman. Jokin on nyt päällä.")
                        kasijarru = True
                    else:
                        print ("Palautatte kahvan alkuperäiseen asentoonsa.")
                        kasijarru = False
                elif numerovalinta == "5":
                    print ("Hytti keinahtaa lievästi.")
                elif numerovalinta == "6":
                    if kasijarru == True or kytkin == False:
                        print ("Mitään ei tapahdu.")
                    else:
                        if suunta == "etelään":
                            print ("Kaivuri liikkuu taaksepäin.")
                            etaisyys += 1
                        elif suunta == "pohjoiseen":
                            if etaisyys == 0:
                                print ("Kaivuri ajaa suoraan seinästä läpi! Ette näe kaaosta, mutta kuulette sen ja tunnette tärinän luuytimissänne. Tämä oli tässä.")
                                seina_hp = 0
                            print ("Kaivuri liikkuu taaksepäin.")
                            etaisyys -= 1
                        elif suunta == "itään" or suunta == "länteen":
                            print ("Kaivuri törmää johonkin. Tähän suuntaan ei voi liikkua.")
                elif numerovalinta == "7":
                    if kytkin == True:
                        print ("Lakkaatte painamasta kytkintä.")
                        kytkin = False
                    else:
                        print ("Kaivuri nytkähtää vähän. Tiedätte sen verran vanhasta teknologiasta, että tunnistatte tämän kytkimeksi. Pidätte sitä pohjassa.")
                        kytkin = True
                elif numerovalinta == "8":
                    if kasijarru == True or kytkin == False:
                        print ("Mitään ei tapahdu.")
                    else:
                        if suunta == "etelään":
                            if etaisyys == 0:
                                print ("Kaivuri ajaa suoraan seinästä läpi! Tuulilasista lentää tiiliä ja laastia, mutta mikään ei osu teihin! Tämä oli tässä.")
                                seina_hp = 0
                            print ("Kaivuri liikkuu eteenpäin.")
                            etaisyys -= 1
                        elif suunta == "pohjoiseen":
                            print ("Kaivuri liikkuu eteenpäin.")
                            etaisyys += 1
                        elif suunta == "itään" or suunta == "länteen":
                            print ("Kaivuri törmää johonkin. Tähän suuntaan ei voi liikkua.")
                elif numerovalinta == "9":
                    if virta == False:
                        print ("Valot välähtävät päälle. Moottori alkaa hurista himmeästi. Toivottavasti tämä laite pysyy vielä vähän aikaa ehjänä.")
                        virta = True
                    else:
                        print ("Kaivuri hiljenee ja hämärtyy taas.")
                        virta = False
                elif numerovalinta == "10":
                    print ("Ajovalot välähtävät hetkeksi päälle, mutta sammuvat heti.")
                elif numerovalinta == "0":
                    return
            self.vaikutusalue.etela_estetty = False