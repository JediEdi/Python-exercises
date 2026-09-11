vuodenajat = ("talvi", "talvi", "kevät", "kevät", "kevät", "kesä", "kesä", "kesä", "syksy", "syksy", "syksy", "talvi")
kuukausi = int(input ("Tämä ohjelma kertoo, mihin vuodenaikaan antamasi kuukausi kuuluu.\nKuukausi kokonaislukuna: "))
print (f"Kuukautesi vuodenaika on {vuodenajat[kuukausi - 1]}")