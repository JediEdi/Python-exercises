class Adventurer():
    adventurers = []
    def __init__(self, name, health_points, stamina, attack_damage):
        self.name = name
        self.health_points = health_points
        self.stamina = stamina
        self.attack_damage = attack_damage

    def gain_life(self, amount):
        self.health_points += amount
        print (f"\n{self.name} gains {amount} health!")

    def lose_life(self, amount):
        if amount >= self.health_points:
            self.health_points = 0
            for party in Party.parties:
                if self in party.members:
                    print (f"\n{self.name} has died! OMG!!!")
                    party.retire_member(self)
        else:
            self.health_points -= amount
            print (f"\n{self.name} takes {amount} damage!")

class Mage(Adventurer):
    def __init__(self, name, health_points = 50, stamina = 100, attack_damage = 20):
        super().__init__(name, health_points, stamina, attack_damage)
        Adventurer.adventurers.append (self.name)

    def party_heal(self):
        for party in Party.parties:
            if self in party.members:
                print (f"\n{self.name} heals everyone in party {party.name}!")
                for adventurer in party.members:
                    adventurer.gain_life(50)
        
class Paladin(Adventurer):
    def __init__(self, name, health_points = 150, stamina = 100, attack_damage = 5):
        super().__init__(name, health_points, stamina, attack_damage)
        Adventurer.adventurers.append (self.name)

class Rogue(Adventurer):
    def __init__(self, name, health_points = 100, stamina = 100, attack_damage = 10):
        super().__init__(name, health_points, stamina, attack_damage)
        Adventurer.adventurers.append (self.name)

class Party():
    parties = []
    def __init__(self):
        self.members = []
        self.name = Party.parties.__len__() + 1
        Party.parties.append (self)

    def add_member(self, adventurer):
        self.members.append (adventurer)
        print (f"\n{adventurer.name} has joined party {self.name}!")

    def retire_member(self, adventurer):
        if adventurer in self.members:
            self.members.remove (adventurer)
            print (f"\n{adventurer.name} has left party {self.name}!")

    def show_members(self):
        print (f"\nIn party {self.name}...")
        for member in self.members:
            print (member.name)

    def show_health(self):
        print (f"\nIn party {self.name}...")
        for member in self.members:
            print (f"{member.name}'s health: {member.health_points}")

adventurer_1 = Paladin("Cerebrus")
adventurer_2 = Mage("Hlin")
adventurer_3 = Rogue("Sam Handwich")

# adventurer_1 = Adventurer(input("Name of the first adventurer: "))
# adventurer_2 = Adventurer(input("Name of the second adventurer: "))
# adventurer_3 = Adventurer(input("Name of the third adventurer: "))

print (f"\nAdventurers {adventurer_1.name}, {adventurer_2.name} and {adventurer_3.name} get together and set out on a quest.")
party = Party()
party.add_member(adventurer_1)
party.add_member(adventurer_2)
party.add_member(adventurer_3)
print (f"\n{adventurer_1.name} has run afoul of a goblin! During the fight, the goblin hits him over the head!")
adventurer_1.lose_life(100)
print (f"\n{adventurer_2.name}, in their ignorance, has eaten a poisonous mushroom!")
adventurer_2.lose_life(20)
print (f"\n{adventurer_3.name} has fallen down a tree in reaching for a treasure chest perched on top!")
adventurer_3.lose_life(50)

party.show_health()
adventurer_2.party_heal()
if adventurer_2 in party.members:
    print (f"\n{adventurer_2.name} has grown weary for the day. They retire into the nearest tavern!")
else:
    print (f"\n{adventurer_2.name} is gone! There will be no healing today!")
party.retire_member(adventurer_2)
party.show_members()
party.show_health()