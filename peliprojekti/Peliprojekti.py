print ("Tervetuloa Evoluutiomiehen maailmaan.")
pelaajan_nimi = input("Mikä on nimenne?\nVastaus: ")
pelaajan_ika = int(input("Mikä on ikänne?\nVastaus kokonaislukuna: "))
print ("\nPelaajan nimi: " + pelaajan_nimi + "\nPelaajan ikä: " + str(pelaajan_ika))
if pelaajan_ika < 12:
    print ("\nOlette alaikäinen. Ette voi pelata.")
else:
    while 1 == 1:
        numerovalinta = input ("\nMinkä komennon haluatte suorittaa?\n1: Pelaa peliä\n2: Asetukset\n3: Poistu pelistä\nVastaus: ")
        if numerovalinta == "1":
            print ("\nKirjoitit kirjaimen ja voitit pelin. Hyvää työtä.")
        elif numerovalinta == "2":
            print ("\nAsetukset on asetettu. Buu jaa.")
        elif numerovalinta == "3":
            print ("\nMoro.")