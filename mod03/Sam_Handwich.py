# Muista imuroida lattiat.
# Ctrl + K + S
# cls terminaalissa tyhjentää sen.
# ctrl + k + c = commentoi
# ctrl + k + u = uncommentoi

## Tässä on teikäläiselle ohjelma, joka kysyy käyttäjältä fahrenheitin ja antaa celsiuksen:
# print ("Helou. Jos on vaikeuksia muuntaa fahrenheit-asteita celsiusasteiksi, olet tullut oikeaan paikkaan.")
# fahrenheit = input("Anna lämpötila fahrenheitteina\nVastaus:")
# celsius = (int(fahrenheit) - 32) * 5 / 9
# # print (fahrenheit + " fahrenheittia ynnää " + str(celsius) + " celsiusta.")
# print(f"Lämpötila fahrenheitteina: {int(fahrenheit):6.2f} Lämpötila celsiuksina: {celsius:6.2f}")

## Poista toinen yhtäsuuruusmerkki. Ilmainen syntax error.
# cat = input("Enter the name of the cat: ")
# dog = input("Enter the name of the dog: ")

# if cat == dog:
#     print("Oh my! The cat and dog have the same name!")

## Hmm. Miksi ei toimi?
# age = int(input("Enter age: "))
# if 15 <= age < 18:
#     weight = float(input("Enter weight (kg): "))
# if (age >= 15 and weight >= 55) or age >= 18:
#     print("The medicine can be used.")

## Juu.
age = int(input("Enter your age: "))
# if age >= 65:
#     print("You are retired.")
# elif age >= 18:
#     print("You are working-age.")
# elif age >= 7:
#     print("You are in school.")
# elif age >= 0:
#     print("You are a small child.")
# else:
#     print ("You can't be of negative age, fool.")
if age >= 65:
    print ("You are retired.")
else:
    if age >= 18:
        print("You are working-age.")
    else:
        if age >= 7:
            print("You are in school.")
        else:
            if age >= 0:
                print("You are a small child.")
            else:
                print ("You can't be of negative age, fool.")

# Pyöritä koodia Run and Debug -valikosta. Breakpoint