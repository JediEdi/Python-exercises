def yksikkomuunnos(gallona):
    print ("Tilavuus litroina: " + str(gallona * 3.785))
gallona = float(input ("Tämä ohjelma muuntaa Yhdysvaltain gallonat litroiksi. Kuinka monta gallonaa haluat muuntaa?\nVastaus numeroina: "))
while gallona >= 0:
    yksikkomuunnos(gallona)
    gallona = float(input ("Tämä ohjelma muuntaa Yhdysvaltain gallonat litroiksi. Kuinka monta gallonaa haluat muuntaa?\nVastaus numeroina: "))