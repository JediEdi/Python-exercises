class Dog:
    def __init__(self, name, birth_year, sound="Woof woof"):
        self.name = name
        self.birth_year = birth_year
        self.sound = sound

    def bark(self, times):
        for i in range(times):
            print(self.name + " barks: " + self.sound)
        return

class Hotel:
    dogs_in_hotels = []
    def __init__(self, name):
        self.dogs = []
        self.name = name

    def dog_checkin(self, dog):
        if dog in self.dogs:
            print (dog.name + " is already in " + self.name)
        else:
            self.dogs.append(dog)
            Hotel.dogs_in_hotels.append(dog)
            print(dog.name + " checked in to " + self.name)
            return

    def dog_checkout(self, dog):
        if dog in self.dogs:
            self.dogs.remove(dog)
            Hotel.dogs_in_hotels.append(dog)

            print(dog.name + " checked out from " + self.name)
        else:
            print (dog.name + " is not in " + self.name)
        return

    def greet_dogs(self):
        print ("At " + self.name + "...")
        for dog in self.dogs:
            dog.bark(1)

# Main program

dog1 = Dog("Rascal", 2018)
dog2 = Dog("Boi", 2022, "Yip yip yip")

hotel1 = Hotel("Hotel Transylvania")

hotel1.dog_checkin(dog1)
hotel1.dog_checkin(dog2)
hotel1.greet_dogs()

hotel1.dog_checkout(dog1)
hotel1.greet_dogs()

hotel2 = Hotel("Dog B&B ⭐⭐⭐⭐⭐")

hotel2.dog_checkin (dog1)
hotel2.greet_dogs()

print ("\n\n")

hotel2.dog_checkin (dog1)
hotel2.dog_checkout (dog2)