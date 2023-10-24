print("<10_1>")

class Elevator:

    def __init__(self, b, t):
        self.bottom = b
        self.top = t
        self.current = b

    def floor_up(self, num):
        for i in range(self.current, num+1):
            print(f"{self.current}F.")
            if self.current == num:
                return
            self.current += 1

    def floor_down(self, num):
        for i in range(self.current, num+1, -1):
            print(f"{self.current}F.")
            if self.current == num:
                return
            self.current -= 1
    def go_to_floor(self, num):
        if num > self.current:
            return self.floor_up(num)
        elif num < self.current:
            return self.floor_down(num)


h=Elevator(1,6)
h.go_to_floor(5)