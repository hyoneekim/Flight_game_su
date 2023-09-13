print("\n6_1\n")

import random

def dice():
    result = random.randint(1,6)
    return result

results = []
count = 1

result = dice()

while (result != 6):
    results.append(result)
    print(f" {count} round's result: {result}")
    count += 1
    result = dice()

print("\n6_2\n")

def dice_custom(num):
    result = random.randint(1,num)
    return result

numAsked = int(input("Enter the number of sides on the dice : "))

results2 = []
count2 = 1
result = dice_custom(numAsked)


while (result != numAsked):
    results2.append(result)
    print(f" {count2} round's result: {result}")
    count2 = count2 + 1
    result = dice_custom(numAsked)

print("\n6_3\n")

def gallon_to_litre(num):
    toLiter = num * 3.78541
    return toLiter

askUser = float(input("How much gallons? Exit by entering negative value: "))

while ( askUser >= 0):
    print(f"{askUser} gallon is {gallon_to_litre(askUser):3f} litres.")
    askUser = float(input("How much gallons? Exit by entering negative value: "))

print("\n6_4\n")

def sum_lst(list):
    sumNum = 0
    for i in list:
        sumNum += i
    return sumNum


lst = [3,4,6,7]
print(sum_lst(lst))

print("\n6_5\n")

def lst_noOdd(list):
    for i in list:
        if (i % 2 !=0):
            list.remove(i)
    return list

numLst = [1,2,3,4,5,6,7,8,9]
print(numLst)
print(lst_noOdd(numLst))

print("\n6_6\n")

import math

def pizza_price(dia,price):
   unitPrice = price / (dia**2 * math.pi) * 100
   return unitPrice


firstDia= float(input("Enter the diameter of the first pizza (cm): "))
firstPrice= float(input("and the price of it (Euro): "))
secondDia= float(input("Enter the diameter of the second pizza (cm): "))
secondPrice= float(input("and the price of it (Euro): "))

print(f"The unit price of the first pizza is {pizza_price(firstDia,firstPrice):.3f} / m^2.")
print(f"The unit price of the second pizza is {pizza_price(secondDia,secondPrice):.3f} / m^2.")

if (pizza_price(firstDia, firstPrice) < pizza_price(secondDia, secondPrice)):
   print("first pizza has better value.")
elif (pizza_price(firstDia, firstPrice) > pizza_price(secondDia, secondPrice)):
   print("The second pizza has better value.")
else:
   print("The pizzas has the same value.")