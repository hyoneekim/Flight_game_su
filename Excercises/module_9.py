print("<9-1>\n")



class Car:

    def __init__(self, n, ms, cs=0, td=0):
        self.num = n
        self.max_speed = ms
        self.current_speed = cs
        self.travelled_distance = td

    def accel(self, speed):
        self.current_speed += speed
        if self.current_speed < 0:
            self.current_speed = 0
        elif self.current_speed > self.max_speed:
            self.current_speed = self.max_speed -1

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours



c1 = Car("ABC-123", 142)
print(f"Registration plate: {c1.num}, Maximum speed: {c1.max_speed}km/h, Current speed: {c1.current_speed}km/h, Travelled distance: {c1.travelled_distance}km")

print("\n<9-2> & <9-3>\n")

c1.accel(30)
c1.drive(1)
print(f"Your current speed: {c1.current_speed}, Travelled distance: {c1.travelled_distance}km")
c1.accel(70)
c1.drive(1)
print(f"Your current speed: {c1.current_speed}, Travelled distance: {c1.travelled_distance}km")
c1.accel(50)
c1.drive(1)
print(f"Your current speed: {c1.current_speed}, Travelled distance: {c1.travelled_distance}km")
c1.accel(-200)
print(f"Emergency Break! Your current speed: {c1.current_speed}, Travelled distance: {c1.travelled_distance}km")

print("\n<9-4>\n")
import random
cars = []
for i in range(10):
    i = Car(f"ABC-{i+1}", random.randint(100,200))
    cars.append(i)
    print(
        f"Registration plate: {i.num}, Maximum speed: {i.max_speed}km/h, Current speed: {i.current_speed}km/h, Travelled distance: {i.travelled_distance}km")




