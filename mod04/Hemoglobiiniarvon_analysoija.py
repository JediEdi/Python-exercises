import time
print ("Tämä ohjelma laskee, onko käyttäjän hemoglobiiniarvo riittävä biologiselle sukupuolelle.")
time.sleep (1)
sukupuoli = input("Mikä on biologinen sukupuolesi?\nVastaus (M / F): ")
if sukupuoli == ("M") or sukupuoli == ("F"):
    hemoglobiiniarvo = float(input("Mikä on hemoglobiinitasosi?\nVastaus (x g/l): "))
    if sukupuoli == ("M") and 195 >= hemoglobiiniarvo >= 134:
        print ("Hemoglobiinitasosi on normaali.")
    elif sukupuoli == ("M") and hemoglobiiniarvo > 195:
        print ("Hemoglobiinitasosi on korkea.")
    elif sukupuoli == ("M") and hemoglobiiniarvo < 134:
        print ("Hemoglobiinitasosi on alhainen.")

    elif sukupuoli == ("F") and 175 >= hemoglobiiniarvo >= 117:
        print ("Hemoglobiinitasosi on normaali.")
    elif sukupuoli == ("F") and hemoglobiiniarvo > 175:
        print ("Hemoglobiinitasosi on korkea.")
    elif sukupuoli == ("F") and hemoglobiiniarvo < 117:
        print ("Hemoglobiinitasosi on alhainen.")
else:
    print ("Sukupuolen on oltava M tai F.")

# Yritin myös mallia:
# if not sukupuoli == ("M") or ("F"):
#   print ("Sukupuolen on oltava M tai F.")
# else:
#   (kaikki muu koodi)
# Mutta ei toiminut. Näin printattiin "Sukupuolen on oltava..." joka kerta. Hmm.