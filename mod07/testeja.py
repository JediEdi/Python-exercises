# def testi(niin):
#     print (kaupunki)
#     if (kaupunki == ("")):
#         print (niin)
# kaupunki = ("Vantaa")
# testi("")
# kaupunki = ("Espoo")
# testi("")
# kaupunki = ("")
# testi("i collect blue chewing gum")

# def greet(greeting, times):
#     for i in range(times):
#         print(greeting + " round: " + str(i+1))
#     return

# greet(("wassaaaap"), 7)

# def sum_of_squares(first, second):
#     mina_lennan = first**2 + second**2
#     return mina_lennan

# number1 = float(input("Enter the first number: "))
# number2 = float(input("Enter the second number: "))
# result = sum_of_squares(number1, number2)
# print(f"The sum of squares for numbers {number1:.3f} and {number2:.3f} is {result:.3f}.")

def inventory(items):
    print("You have the following items:")
    for item in items:
        print("◦ " + item)
        if item == ("Swiss Army Knife"):
            print ("    You get the feeling the Swiss Army Knife could be useful...")
        if item == ("Map"):
                    print ("    Too bad it's a map of the wrong planet...")
    return

backpack = ["Water bottle", "Map", "Compass"]
inventory(backpack)
backpack.append("Swiss Army Knife")
backpack.append("Fungus")
inventory(backpack)

# def sum(*numbers):
#     total = 0
#     for n in numbers:
#         total += n
#     return total

# print("Sum is", sum(1, 2, 3))

# def greet(greeting="Hello", times=1):
#     for i in range(times):
#         print(greeting + " " + str(i+1) + ". time")
#     return

# greet()
# greet("Hi", 3)