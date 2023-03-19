# class Animal:
#     def __init__(self, name, legs_count, eyes_count):
#         self.legs_count = float(legs_count)
#         self.eyes_count = float(eyes_count)
#         self.name = name
#         self.is_alive = True
#
#     def __str__(self):
#         return self.name
#
# class Dog(Animal):
#     def __init__(self, name, legs_count, eyes_count, spieces):
#         super().__init__(name, legs_count, eyes_count)
#         self.spieces = spieces
#
#     def __str__(self):
#         return f"{super().__str__()} - {self.spieces}"
#
# a1 = Animal("Koczkodan", 4, 2)
# d1 = Dog("Pączek", 4, 2, "Mops")
# print(str(d1))
# print(str(a1))




class Person:
    def __init__(self, name, surname, address, age):
        self.name = name
        self.surname = surname
        self.address = address
        self.age = int(age)

    def __str__(self):
        return f"{self.surname} {self.name} {self.address}"

    def check_is_adult(self):
        if self.age >= 18:
            return True

class Customer(Person):
    def __init__(self, name, surname, address, age, login):
        super().__init__(name, surname, address, age)
        self.login = login
        self.orders = []
        self.total_order_cost = 0.0

    def __str__(self):
        return f"{self.login} {super().__str__()}"

    def add_order(self,product: str, cost: float):
        if self.age >= 18:
            self.orders.append((product, cost))
            self.total_order_cost += cost
        else:
            return "You are underaged and can'r order!"

    def show_order(self):
        for e in self.orders:
            print(e)




p1 = Person("Jan", "Kowalski", "ul. Zielona 1 77-100 Bytów", 25)
print(p1.check_is_adult())
print(str(p1))

p2 = Customer("Grażyna", "Nowak", "ul. Pochyła 17 77-100 Bytów", 38, "kochamkotki38")
print(str(p2))
p2.add_order("Czekolada", 5.99)
p2.add_order("Sok owocowy", 4.89)
print(p2.show_order())

# start - godzina rozpoczęcia seansu
# playtime - ile sekund oglądaliśmy
#
# Program ma podzielić playtime na poszczególne grupy
#
# p = 3.5
# s = 5.6
#
# 5: 0.4 (do 6)
# 6: 1.0 (do 7)
# 7: 1.0 (do 8)
# 8: 1.0 (do 9)
# 9: 0.1 (do 10) <-- p + s
#
# 0: 0.0 - 1.00
# 1: 1.01 - 2.00
# 2: 2.01 - 3.00
# ...
# 10: 10.01 - 11.00


def time_split(start: float, playtime: float):
    start_hour = int(start)
    end = start + playtime
    end_hour = int(end)