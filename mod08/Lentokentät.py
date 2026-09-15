lentoasemat = [
    {
        "nimi": "Nummela",
        "icao": "EFNY"
    },
    {
        "nimi": "Helsinki-Vantaa",
        "icao": "EFHK"
    },
    {
        "nimi": "Turku",
        "icao": "EFTU"
    }
]

def valikko():
    numerovalinta = input ("\nMitä tahdot tehdä?\n1. Hae lentoasemaa ICAO-koodilla.\n2. Lisää uusi lentoasema syöttämällä ICAO-koodi ja nimi.\n3. Poistu.\nValinta: ")
    if numerovalinta == ("1"):
        haettu_koodi = input ("ICAO-koodi isoin kirjaimin: ")
        for asema in lentoasemat:
            if asema["icao"] == haettu_koodi:
                print (asema["nimi"])
        valikko()
    elif numerovalinta == ("2"):
        syotetty_koodi = input ("\nLentoaseman ICAO-koodi isoin kirjaimin: ")
        syotetty_nimi = input ("\nLentoaseman nimi isolla alkukirjaimella: ")
        uusi_lentoasema = {"nimi": syotetty_nimi,
                           "icao": syotetty_koodi}
        lentoasemat.append (uusi_lentoasema)
        valikko()

print ("Tämän ohjelman avulla voit hakea lentoasemaa ICAO-koodin perusteella tai lisätä listaan uuden lentoaseman syöttämällä sen ICAO-koodin ja nimen.")
valikko()