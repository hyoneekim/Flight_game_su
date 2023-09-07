import random
print("5_1\n")
numbers = []
howMany = 0
sumOfNums = 0
ask = int(input("How many dice to roll?: "))
while (howMany < ask):
    numbers.append(random.randint(1, 6))
    howMany = howMany + 1

print(numbers)
for n in numbers:
    sumOfNums = sumOfNums + n

print(f"the sum of number is {sumOfNums}.")

print("\n5_2\n")

askNum = input("Enter a number or quit by enter space. ")
receivedNum = []

while(askNum != " "):
    receivedNum.append(int(askNum))
    askNum = input("Enter a number or quit by enter space. ")

receivedNum.sort(reverse=True)
print(f"The five greatest numbers are: \n {receivedNum[0:5]}")

print("\n5_3\n")

whatNum = int(input("Enter an integer number: "))
numRange = []

for n in range(2,whatNum):
    if(whatNum % n == 0) :
        numRange.append(n)

if len(numRange) == 0:
    print(f"{whatNum} is a prime number.")
else:
    print(f"{whatNum} isn't a prime number, and it's also divisible by {numRange}.")


print("\n5_4\n")

cities = []

for city in range(5):
    askCity = input("Enter a city: ")
    cities.append(askCity)

for n in cities:
    print(n)

