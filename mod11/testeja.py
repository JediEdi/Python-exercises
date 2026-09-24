# class Employee:

#     total_employees = 0

#     def __init__(self, first_name, last_name):
#         Employee.total_employees = Employee.total_employees + 1
#         self.employee_number = Employee.total_employees
#         self.first_name = first_name
#         self.last_name = last_name

#     def print_information(self):
#         print(f"{self.employee_number}: {self.first_name} {self.last_name}")

# class HourlyPaid(Employee):

#     def __init__(self, first_name, last_name, hourly_pay):
#         self.hourly_pay = hourly_pay
#         Employee.__init__(self, first_name, last_name)

#     def print_information(self):
#         super().print_information()
#         print(f"Hourly pay: {self.hourly_pay}")

# class MonthlyPaid(Employee):

#     def __init__(self, first_name, last_name, monthly_pay):
#         self.monthly_pay = monthly_pay
#         Employee.__init__(self, first_name, last_name)

#     def print_information(self):
#         super().print_information()
#         print(f"Monthly pay: {self.monthly_pay}")


# employees = []
# employees.append(HourlyPaid("Viivi", "Virta", 12.35))
# employees.append(MonthlyPaid("Ahmed", "Habib", 2750))
# employees.append(Employee("Pekka", "Puro"))
# employees.append(HourlyPaid("Olga", "Glebova", 14.92))

# for e in employees:
#     e.print_information()

# print (__name__)


# import random

# class Varusmies():
#     def __init__(self, nimi, sukunimi):
#         self.nimi = nimi
#         self.sukunimi = sukunimi

#     def ilmoita_tiedot(self):
#         print (f"- Herra alikersantti, tykkimies {self.sukunimi}. Voinko korjata?\n- Ette voi, {self.nimi}.")

# class Miehisto(Varusmies):
#     def __init__(self, nimi, sukunimi, arvo):
#         super().__init__(nimi, sukunimi)
#         self.arvo = arvo

#     def ilmoita_tiedot(self):
#         print (f"- Herra laivan kokki, {self.arvo} {self.sukunimi}, voinko mennä uimaan?")
#         print (f"- Ette voi, {self.nimi}.")

# class Henkilokunta(Miehisto):
#     def __init__(self, nimi, sukunimi, arvo, tehtava):
#         super().__init__(nimi, sukunimi, arvo)
#         self.tehtava = tehtava
#         self.aseen_numero = (random.randint(100000, 999999))

#     def ilmoita_tiedot(self):
#         super().ilmoita_tiedot()
#         print (self.tehtava)
#         print (self.aseen_numero)


# varusmies1 = Varusmies("Sam", "Handwich")
# varusmies1.ilmoita_tiedot()

# print ("")

# varusmies2 = Miehisto("Homo", "Jorma", "Fiskeplaske")
# varusmies2.ilmoita_tiedot()

# print ("")

# henk1 = Henkilokunta("Lady", "Gagga", "Julggis", "Tylsistyttäminen")
# henk1.ilmoita_tiedot()

class Isa():
    def __init__(self, auto):
        self.auto = auto

class Aiti():
    def __init__(self, ruoka):
        self.ruoka = ruoka

class Mina(Isa, Aiti):
    def __init__(self, nimi, auto, ruoka):
        Isa.__init__(self, auto) # ILMAN SUPERIA PITÄÄ PASSATA SELF!
        Aiti.__init__(self, ruoka) # ILMAN SUPERIA PITÄÄ PASSATA SELF!
        self.nimi = nimi
        self.kaikki = (Isa.auto + Aiti.ruoka)

meikalainen = Mina("Jonne", "Saab", "Maksalaatikko")
print (meikalainen.nimi)
print (meikalainen.auto)
print (meikalainen.ruoka)
print (meikalainen.kaikki)