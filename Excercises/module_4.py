#4_1

num = 1
while (num < 1001):
    if (num % 3 == 0):
        print(num)
    num = num + 1

#4_2

enterInch = float(input("Enter a number in inch: "))
while (enterInch > 0):
    toCm = enterInch * 2.54
    print(f"converted to cm : {toCm} cm")
    enterInch = float(input("Enter a number in inch: "))

print("Program ended.")

#4_3

askNum = input("Enter a number: ")
receivedNum = float(askNum)
receivedMin = receivedNum
receivedMax = receivedNum
askNum = input("Enter a number: ")
while (askNum != " "):
    receivedNum = float(askNum)
    if ( receivedNum < receivedMin):
        receivedMin = receivedNum
    elif (receivedNum > receivedMax):
        receivedMax = receivedNum
    askNum = input("Enter a number: ")
print(f"The smallest number is {receivedMin} and the largest is {receivedMax}.")

#4_4

import random

drawNum = random.randint(1,10)
#to check if this game draws a number only once between guesses.
#print(drawNum)
guessNum = int(input("Guess the number between 1 and 10: "))
while (drawNum != guessNum):
    if (guessNum < drawNum):
        print("Too low. try again.")
        guessNum = int(input("Guess the number between 1 and 10: "))
    elif (guessNum > drawNum):
        print("Too high. try again.")
        guessNum = int(input("Guess the number between 1 and 10: "))

print("You got it correct!")

#4_5

userID = "python"
userPW = "rules"

signInID = input("Enter your ID: ")
signInPW = input("Enter your password: ")

trialCount = 0
while (trialCount < 4):
    if (signInID == userID and signInPW == userPW):
        print("Welcome")
        break
    else:
        print(f"incorrect ID or password. Try again. Attempt left : {4-trialCount}")
        signInID = input("Enter your ID: ")
        signInPW = input("Enter your password: ")
        trialCount = trialCount +1
if (trialCount == 4):
    print("Access denied.")

#4_6

askPoints = int(input("How many random points you'd like to generate?: "))
countPoints = 0
pointsInCircle = 0
while ( countPoints < askPoints ):
    pointOfX = random.uniform(-1,1)
    pointOfY = random.uniform(-1,1)
    #to check if the points are generated normally
    #print(f"{pointOfX},{pointOfY}")
    countPoints = countPoints +1
    if (pointOfX ** 2 + pointOfY ** 2 < 1):
        pointsInCircle = pointsInCircle + 1
approxOfPi = 4 * pointsInCircle / askPoints
print(f"Approximation of Pi is {approxOfPi}.")


