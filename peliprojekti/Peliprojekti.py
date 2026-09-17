custom_nimet = set() # setti on ehkä buginen. nimet on vaan muuttujia? canon nimi on muuttujan nimi, arvo on joko canon nimi tai randomoitu
# pelaajan_nimi = ("Testeri") # DEBUG - LAITA POIS LOPULLISESSA VERSIOSSA
# pelaajan_ika = 20 # DEBUG - LAITA POIS LOPULLISESSA VERSIOSSA
def paavalikko():
    numerovalinta = input ("\nMinkä komennon haluatte suorittaa?\n1: Pelaa peliä\n2: Asetukset\n3: Poistu pelistä\nVastaus: ")
    if numerovalinta == "1":
        print ("\nKirjoitit kirjaimen ja voitit pelin. Hyvää työtä.")

    elif numerovalinta == "2":
        numerovalinta = input ("\nMinkä asetuksen haluatte muuttaa?\n0: Palaa päävalikkoon\n1: Lisää nimiä peliin\n2. Tarkista nimilista\nVastaus: ")
        if numerovalinta == "0":
            paavalikko ()
        elif numerovalinta == "1":
            print ("\nVoitte lisätä tänne nimiä, joita saatetaan satunnaisesti määrittää pelin hahmoille. Jättäkää lista tyhjäksi säilyttääksenne 'viralliset' nimet.\nKirjoittakaa nimi ja painakaa enteriä jokaisen nimen jälkeen. Painakaa enteriä kirjoittamatta mitään, jos tahdotte poistua.")
            custom_nimi = input ("Nimi: ")
            if custom_nimi != (""):
                custom_nimet.add (custom_nimi)
            else:
                paavalikko()
            while custom_nimi != (""):
                custom_nimi = input ("Kirjoittakaa nimi tai palatkaa päävalikkoon tyhjällä merkkijonolla: ")
                if custom_nimi != (""):
                    custom_nimet.add (custom_nimi)
                else:
                    return custom_nimet
        elif numerovalinta == "2":
            print ("\n" + str(custom_nimet))
            paavalikko()

    elif numerovalinta == "3":
        print ("\nMoro.")

print ("Tervetuloa Evoluutiomiehen maailmaan.")
pelaajan_nimi = input("Mikä on nimenne?\nVastaus: ") # DEBUG - LAITA PÄÄLLE LOPULLISESSA VERSIOSSA
pelaajan_ika = int(input("Mikä on ikänne?\nVastaus kokonaislukuna: ")) # DEBUG - LAITA PÄÄLLE LOPULLISESSA VERSIOSSA
print (f"\nPelaajan nimi: {pelaajan_nimi} \nPelaajan ikä: {pelaajan_ika} ")
if pelaajan_ika < 12:
    print ("\nOlette alaikäinen. Ette voi pelata.")
else:
    custom_nimet = paavalikko()
    paavalikko() # korjaa joskus. kolmonen pitää valita kaksi kertaa, jotta poistuisi