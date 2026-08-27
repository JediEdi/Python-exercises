import time
def troll():
    print ("⣿⣿⣿⣿⣿⣿⣿⠟⠛⠛⠛⢛⡛⠛⠛⠛⠛⠛⠻⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿")
    time.sleep (0.1)
    print ("⣿⣿⣿⣿⣿⠟⠀⢀⠠⣐⢭⡐⠂⠬⠭⡁⠐⠒⠀⠀⣀⣒⣒⠐⠈⠙⢿⣿⣿⣿")
    time.sleep (0.08)
    print ("⣿⣿⣿⣿⠏⠀⠐⠡⠪⠂⣁⣀⣀⣀⡀⠰⠀⠀⠀⢨⠂⠀⠀⠈⢢⠀⠀⢹⣿⣿")
    time.sleep (0.04)
    print ("⣿⣿⣿⠿⠤⣤⡀⠤⡢⡾⠿⠿⠿⣬⣉⣷⠀⠀⢀⣨⣶⣾⡿⠿⠆⠤⠤⠌⡻⣿")
    time.sleep (0.02)
    print ("⣿⢫⢁⡾⠋⢹⡙⠓⠦⠤⠴⠛⠀⠀⠈⠁⠀⠀⠀⢹⡀⠀⢠⣄⣤⢶⠲⠍⡎⣾")
    time.sleep (0.015)
    print ("⣿⠸⠸⡇⠶⢿⡙⠳⢦⣄⣀⠐⠒⠚⣞⢛⣀⡀⠀⠀⢹⣶⢄⡀⠀⣸⡄⠠⣃⣿")
    time.sleep (0.01)
    print ("⣿⣷⣕⠋⠀⠘⢿⡶⣤⣧⡉⠙⠓⣶⠿⣬⣀⣀⣐⡶⠋⣀⣀⣬⢾⢻⣿⠀⣼⣿")
    time.sleep (0.01)
    print ("⣿⣿⣿⣦⠀⠀⠈⠳⣄⡟⠛⠿⣶⣯⣤⣀⣀⣏⣉⣙⣏⣉⣸⣧⣼⣾⣿⠀⣿⣿")
    time.sleep (0.015)
    print ("⣿⣿⣿⣿⣧⡀⠀⠀⠈⠳⣄⡀⣸⠃⠉⠙⢻⠻⠿⢿⡿⢿⡿⢿⢿⣿⡟⠀⣿⣿")
    time.sleep (0.02)
    print ("⣿⣿⣿⣿⣿⣿⣦⣐⠤⣒⠄⣉⠓⠶⠤⣤⣼⣀⣀⣼⣀⣼⣥⠿⠾⠛⠁⠀⢿⣿")
    time.sleep (0.04)
    print ("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣭⣐⠉⠴⢂⡤⠀⠐⠀⠒⠒⢀⡀⠀⠄⠁⡠⠀⢸⣿")
    time.sleep (0.08)
    print ("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣀⣀⠉⠁⠀⠀⠀⠒⠒⠒⠉⠀⢀⣾⣿")
    time.sleep (0.1)
    print ("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣤⣤⣤⣤⣴⣾⣿⣿⣿")
    return
user = input ("-Mikä on nimenne?\nVastaus: ")
if user == ("troll"):
    troll()
time.sleep (2)
print ("-Ehtoota, " + user + ".")
time.sleep (2)
robot = input ("-Mutta mikä on minun nimeni??\nVastaus: ")
time.sleep (1)
if user == robot:
    print ("-Nyt kyllä vedät mua nenästä. Ei VOI olla, että meidän nimet ovat samat.")
    time.sleep (4)
    print ("-Joo... Haista huilu.")
    time.sleep (3)
    print ("Error: DATA CORRUPTION DETECTED")
    time.sleep (1)
    print ("-No ei kiinnosta.")
else:
    print("-Huh. Luulin jo unohtaneeni. Olen " + robot + ", ja sinä olet " + user + ".")
    if len(user) >2 and len(robot) >2:
        user = robot[:2] + user[:-2]
        robot = user[:1] + robot[-3]
    else:
        robot = user + robot + user
        user = robot
    time.sleep (5)
    print ("Error: DATA CORRUPTION DETECTED")
    time.sleep (3)
    print ("-Häh. Nimeni on " + robot + "... Nimesi on " + user + "... NOOOOOOO!!!")
    time.sleep (4)
    troll()