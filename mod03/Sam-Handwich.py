# Muista imuroida lattiat.
# Ctrl + K + S
# cls terminaalissa tyhjentää sen.

# Tässä on teikäläiselle ohjelma, joka kysyy käyttäjältä fahrenheitin ja antaa celsiuksen:
print ("Helou. Jos on vaikeuksia muuntaa fahrenheit-asteita celsiusasteiksi, olet tullut oikeaan paikkaan.")
fahrenheit = input("Anna lämpötila fahrenheitteina\nVastaus:")
celsius = (int(fahrenheit) - 32) * 5 / 9
print (fahrenheit + " fahrenheittia ynnää " + str(celsius) + " celsiusta.")