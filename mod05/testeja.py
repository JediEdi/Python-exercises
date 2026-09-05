# nimet = []
# def lista():
#     komento = input ("Mitä haluat tehdä?\n1. lisää nimiä\n2. poista nimiä\n ")
#     if komento == ("1"):
#         komento = input ("Kirjoita nimi, paina enter, jos haluat takaisin.\n ")
#         while komento != (""):
#             nimet.append (komento)
#             komento = input ("Kirjoita nimi, paina enter, jos haluat takaisin.\n ")
#         print (nimet)
#     elif komento == ("2"):
#         komento = input ("Kirjoita nimi, paina enter, jos haluat takaisin.\n ")
#         while komento != (""):
#             nimet.remove (komento)
#             komento = input ("Kirjoita nimi, paina enter, jos haluat takaisin.\n ")
#         print (nimet)
# while 1 == 1:
#     lista()
# # while komento != "MAYDAY"):
# #     lista()

# kaupungit = ["Helsinki", "Espoo", "Vantaa"]
# kaupungit.append ("Porvoo")
# print (kaupungit)
# print (kaupungit[-5])

luvut = [3, 8, 2, 10, 5]
for luku in luvut:
    if luku > 5:
        print (luku)