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

    def run_elevator(self, des):
        for index, ele in enumerate(self.elevators, start = 1):
            print(f"<Elevator No.{index}>")
            ele.go_to_floor(des)

b = Building(-3,13,3)
b.run_elevator(3)

print("\n<10_3>\n")