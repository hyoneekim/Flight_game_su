#2
import math

#2_1
name = input("Insert your name here: \n")
print(f"Hello, {name}!")

#2_2
radius = float(input("Type radius: "))
areaOfCircle = math.pi * radius ** 2
print(f"Area of circle: {areaOfCircle:.4f}")

#2_3

length = float(input("Type length: "))
width = float(input("Type width: "))
perimeterOfRectangle = 2*length + 2* width
areaOfRectangle = length * width
print(f"The perimeter is {perimeterOfRectangle} and the area is {areaOfRectangle}.")

#2_4

firstNum = int(input("Enter the first integer: "))
secondNum = int(input("Enter the second integer: "))
thirdNum = int(input("Enter the last integer: "))

sumOfThree = firstNum + secondNum + thirdNum
productOfThree = firstNum * secondNum * thirdNum
aveOfThree = sumOfThree / 3
print(f"Here are the result. \nThe sum: {sumOfThree}, The product: {productOfThree}, The average: {aveOfThree}.")

#2_5

talents = float(input("Enter talents:\n"))
pounds = float(input("Enter pounds:\n"))
lots = float(input("enter lots:\n"))

talentsToGrams = talents *20*32*13.3
poundsToGrams = pounds * 32*13.3
lotsToGrams = lots * 13.3

inTotal = talentsToGrams + poundsToGrams + lotsToGrams
kilo = int(str(inTotal)[:2])
gram = inTotal-kilo * 1000
print(f"The weight in modern units: {kilo} kilograms and {gram:.2f} grams.")