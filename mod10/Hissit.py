class Hissi():
    def __init__(self, alin_kerros, ylin_kerros, nykyinen_kerros = 1):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        nykyinen_kerros = alin_kerros
        self.nykyinen_kerros = nykyinen_kerros

    def siirry_kerrokseen(self, kerros):
            kerrosero = kerros - self.nykyinen_kerros
            if kerrosero > 0:
                for k in range(kerrosero): 
                    self.kerros_ylos()
            elif kerrosero < 0:
                 for k in range(-1 * kerrosero):
                     self.kerros_alas()
            else:
                print (f"Hissi on jo kerroksessa {self.nykyinen_kerros}.")

    def kerros_ylos(self):
        if self.nykyinen_kerros < self.ylin_kerros:
            self.nykyinen_kerros = self.nykyinen_kerros + 1
            print (f"Hissi siirtyi kerroksen ylös. Kerros on nyt {self.nykyinen_kerros}.")

    def kerros_alas(self):
        if self.nykyinen_kerros > self.alin_kerros:
            self.nykyinen_kerros = self.nykyinen_kerros - 1
            print (f"Hissi siirtyi kerroksen alas. Kerros on nyt {self.nykyinen_kerros}.")


class Talo():
    def __init__(self, alin_kerros, ylin_kerros, hissien_lukumaara):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissien_lukumaara = hissien_lukumaara
        self.hissit_talossa = []
        for hissi in range(hissien_lukumaara):
            hissi = Hissi(alin_kerros, ylin_kerros)
            self.hissit_talossa.append (hissi)

    def ohjaa_hissia(self, hissin_indeksi, kerros):
        self.hissit_talossa[hissin_indeksi].siirry_kerrokseen(kerros)

    def palohalytys(self):
        print ("\nPalohälytys! Hissit siirtyvät pohjakerrokseen!\n")
        for hissi in range(0, self.hissien_lukumaara):
            self.ohjaa_hissia(hissi, self.alin_kerros)


# alin_kerros = int(input ("Mikä on hissin alin kerros?\nVastaus kokonaislukuina: "))
# ylin_kerros = int(input ("Mikä on hissin ylin kerros?\nVastaus kokonaislukuina: "))

# hissi = Hissi(alin_kerros, ylin_kerros)

# kerroskomento = int(input ("Mihin kerrokseen haluat hissin siirtyvän?\nVastaus kokonaislukuina: "))

# hissi.siirry_kerrokseen(kerroskomento)

# print ("\nHissi siirtyy nyt alimpaan kerrokseen.\n")

# hissi.siirry_kerrokseen(alin_kerros)


alin_kerros = int(input ("Mikä on talon alin kerros?\nVastaus kokonaislukuina: "))
ylin_kerros = int(input ("Mikä on talon ylin kerros?\nVastaus kokonaislukuina: "))
hissien_lukumaara = int(input ("Kuinka monta hissiä haluat taloon?\nVastaus kokonaislukuina: "))

talo = Talo(alin_kerros, ylin_kerros, hissien_lukumaara)

hissikomento = int(input ("Mitä talon hisseistä haluat ohjata?\nVastaus kokonaislukuina (väliltä 0 --" + str(hissien_lukumaara - 1) + "): "))
kerroskomento = int(input ("Mihin kerrokseen haluat hissin?\nVastaus kokonaislukuina: "))

talo.ohjaa_hissia(hissikomento, kerroskomento)

hissikomento = int(input ("Mitä talon hisseistä haluat ohjata?\nVastaus kokonaislukuina (väliltä 0 --" + str(hissien_lukumaara - 1) + "): "))
kerroskomento = int(input ("Mihin kerrokseen haluat hissin?\nVastaus kokonaislukuina: "))

talo.ohjaa_hissia(hissikomento, kerroskomento)

talo.palohalytys()