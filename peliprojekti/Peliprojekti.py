def paavalikko():
    numerovalinta = input ("\nMinkä komennon haluatte suorittaa?\n1: Pelaa peliä\n2: Asetukset\n3: Poistu pelistä\nVastaus: ")
    if numerovalinta == "1":
        print ("\nKirjoitit kirjaimen ja voitit pelin. Hyvää työtä.")

    elif numerovalinta == "2":
        numerovalinta = input ("\nMinkä asetuksen haluatte muuttaa?\n0: Palaa päävalikkoon\n1: Lisää nimiä peliin\nVastaus: ")
        if numerovalinta == "0":
            paavalikko ()
        elif numerovalinta == "1":
            print ("\nVoitte lisätä tänne nimiä, joita saatetaan satunnaisesti määrittää pelin hahmoille. ")

    elif numerovalinta == "3":
        print ("\nMoro.")

print ("Tervetuloa Evoluutiomiehen maailmaan.")
pelaajan_nimi = input("Mikä on nimenne?\nVastaus: ")
pelaajan_ika = int(input("Mikä on ikänne?\nVastaus kokonaislukuna: "))
print ("\nPelaajan nimi: " + pelaajan_nimi + "\nPelaajan ikä: " + str(pelaajan_ika))
if pelaajan_ika < 12:
    print ("\nOlette alaikäinen. Ette voi pelata.")
else:
    paavalikko()