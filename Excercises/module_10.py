import random
print("<10_1>")

class Elevator:

    def __init__(self, b, t):
        self.bottom = b
        self.top = t
        self.current = b

    def floor_up(self, num):
        print("Going up..")
        for i in range(self.current, num+1):
            print(f"{self.current}F.")
            if self.current == num:
                return print(f"current floor: {self.current}F.\n")
            self.current += 1

    def floor_down(self, num):
        print("Going down..")
        for i in range(self.current, num-1, -1):
            print(f"{self.current}F.")
            if self.current == num:
                return print(f"current floor: {self.current}F.\n")
            self.current -= 1
    def go_to_floor(self, num):
        if num > self.current:
            return self.floor_up(num)
        elif num < self.current:
            return self.floor_down(num)
        else:
            return print("You are already on the floor.")


h=Elevator(1,6)
h.go_to_floor(5)
h.go_to_floor(2)

print("\n<10_2>\n")

class Building:

    def __init__(self, b, t, n):
        self.bottom = b
        self.top = t
        self.num_ele = n
        self.elevators = []
        for i in range(n):
            i = Elevator(b,t)
            self.elevators.append(i)

    def run_elevator(self, which, des):
        print(f"Moving the elevator No.{which} to the {des} floor..")
        which = self.elevators[which-1]
        which.go_to_floor(des)

    def fire_alarm(self):
        print("Fire alarm has been set off. Moving all the elevators to the bottom floor..")
        for index, ele in enumerate(self.elevators, start = 1):
            print(f"<Elevator No.{index}>")
            ele.go_to_floor(self.bottom)



b = Building(-3,13,3)
b.run_elevator(2,3)
b.run_elevator(3,11)
b.run_elevator(3,6)

print("\n<10_3>\n")

b.fire_alarm()

print("\n<10_4>\n")

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
            
class Race:
    def __init__(self, n, d):
        self.name = n
        self.distance = d
        self.cars = []
        for i in range(10):
            i = Car(f"ABC-{i + 1}", random.randint(100, 200))
            self.cars.append(i)

    hours = 1
    def hour_passes(self):
        for car in self.cars:
            car.accelerate()
            car.drive()
        Race.hours += 1

    def print_status(self):
        print(f"\nResult after {Race.hours} hours:\n")
        for car in self.cars:
            print(f"car {car.num}: Maximum speed: {car.max_speed}km/h, Current speed: {car.current_speed}km/h, Travelled distance: {car.travelled_distance}km")

    def race_finished(self):
        for car in self.cars:
            if car.travelled_distance > self.distance:
                return True

r = Race("Grand Demolition Derby", 8000)

finished = False
while not finished:
    r.hour_passes()
    if Race.hours % 10 == 0:
        r.print_status()
    if r.race_finished() == True:
        finished = True
        r.print_status()

