import time
print ("Tämä ohjelma tulostaa kuvauksen antamastasi laivan hyttiluokasta.")
time.sleep (1)
hyttiluokka = input("Mikä on laivan hyttiluokka?\nVastaus (LUX / A / B / C): ")
if hyttiluokka == ("LUX"):
    print ("LUX on parvekkeellinen hytti yläkannella.")
elif hyttiluokka == ("A"):
    print ("A on ikkunallinen hytti autokannen yläpuolella.")
elif hyttiluokka == ("B"):
    print ("B on ikkunaton hytti autokannen yläpuolella.")
elif hyttiluokka == ("C"):
    print ("C on ikkunaton hytti autokannen alapuolella.")
else:
    print ("Virheellinen hyttiluokka.")