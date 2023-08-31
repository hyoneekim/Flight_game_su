#2
import math

print("\n2_1\n")

name = input("Insert your name here: \n")
print(f"Hello, {name}!")

print("\n2_2\n")
radius = float(input("Type radius: "))
areaOfCircle = math.pi * radius ** 2
print(f"Area of circle: {areaOfCircle:.4f}")

print("\n2_3\n")

length = float(input("Type length: "))
width = float(input("Type width: "))
perimeterOfRectangle = 2*length + 2* width
areaOfRectangle = length * width
print(f"The perimeter is {perimeterOfRectangle} and the area is {areaOfRectangle}.")

print("\n2_4\n")

firstNum = int(input("Enter the first integer: "))
secondNum = int(input("Enter the second integer: "))
thirdNum = int(input("Enter the last integer: "))

sumOfThree = firstNum + secondNum + thirdNum
productOfThree = firstNum * secondNum * thirdNum
aveOfThree = sumOfThree / 3
print(f"Here are the result. \nThe sum: {sumOfThree}, The product: {productOfThree}, The average: {aveOfThree}.")

print("\n2_5\n")

talents = float(input("Enter talents:\n"))
pounds = float(input("Enter pounds:\n"))
lots = float(input("enter lots:\n"))

talentsToGrams = talents *20*32*13.3
poundsToGrams = pounds * 32*13.3
lotsToGrams = lots * 13.3

inTotal = talentsToGrams + poundsToGrams + lotsToGrams
kilo = int(str(inTotal)[:2])
gram = inTotal-kilo * 1000
print(f"The weight in modern units: \n{kilo} kilograms and {gram:.2f} grams.")

print("\n2_6\n")
import random

input("Random code drawer. Press enter when you're ready: ")

firstDigit = random.randint(0,9)
secondDigit = random.randint(0,9)
thirdDigit = random.randint(0,9)

print(f"Here is your new 3-digit code: {firstDigit}{secondDigit}{thirdDigit}")

firstDigitFour = random.randint(1,6)
secondDigitFour = random.randint(1,6)
thirdDigitFour = random.randint(1,6)
fourthDigitFour = random.randint(1,6)

print(f"Here is your new 4-digit code: {firstDigitFour}{secondDigitFour}{thirdDigitFour}{fourthDigitFour}")