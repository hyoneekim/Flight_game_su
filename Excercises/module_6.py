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
    count = count + 1
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

askUser = float(input("How much gallons?: "))

while ( askUser >= 0):
    print(f"{askUser} gallon is {gallon_to_litre(askUser):3f} litres.")
    askUser = float(input("How much gallons?: "))

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