import random
print("<11_1>\n")

class Publication:
    def __init__(self, name):
        self.name = name

    def print_information(self):
        print(f"Name: {self.name}")

class Book(Publication):

    def __init__(self, name, author, page):
        super().__init__(name)
        self.author = author
        self.page = page

    def print_information(self):
        super().print_information()
        print(f"Author: {self.author}, Page: {self.page}")

class Magazine(Publication):
    def __init__(self, name, editor):
        super().__init__(name)
        self.editor = editor

    def print_information(self):
        super().print_information()
        print(f"Chief Editor: {self.editor}")

p =[]
p.append( Magazine("Donald Duck", "Aki Hyyppä"))
p.append( Book("Compartment No. 6", "Rosa Liksom", 192))
for i in p:
    i.print_information()


print("\n<11_2>\n")

class Car:

    def __init__(self, n, ms, cs=0, td=0):
        self.num = n
        self.max_speed = ms
        self.current_speed = cs
        self.travelled_distance = td

    def drive(self, hours =1):
        self.travelled_distance += self.current_speed * hours

    def accelerate(self):
        speed = random.randint(-10,15)
        self.current_speed += speed
        if self.current_speed < 0:
            self.current_speed = 0
        elif self.current_speed > self.max_speed:
            self.current_speed = self.max_speed - 1

class ElectricCar(Car):
    def __init__(self, n, ms, cap):
        super().__init__(n, ms)
        self.capacity = cap

class GasolineCar(Car):
    def __init__(self, n, ms, vol):
        super().__init__(n, ms)
        self.volume = vol

