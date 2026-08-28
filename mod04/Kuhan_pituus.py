import time
print ("Tämä ohjelma kertoo, onko kalastamasi kuhan pituus sallittujen rajojen sisällä.")
time.sleep (1)
kuhan_pituus = float(input("Kuinka pitkä kuha on kyseessä?\nVastaus senttimetreinä: "))
if kuhan_pituus <37:
    print ("Kuha on " + str((37 - kuhan_pituus)) + " senttimetriä alamittainen, ja täytyy laskea takaisin järveen.")