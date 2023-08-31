print("\n3_1\n")

ask = float(input("Enter the length of a zander you caught in cm: "))
short = 42-ask
if (ask >= 42):
    print(f"Congrats! You have caught a zander that is {ask} centimeter long.")
else:
    print(f"You need to release the fish back, it's {short} centimeter short from the size limit.")

print("\n3_2\n")

cabinClass = input("Please enter the name of your class: ")
if (cabinClass == "LUX"):
    print("upper-deck cabin with a balcony.")
elif (cabinClass == "A"):
    print("above the car deck, equipped with a window.")
elif (cabinClass == ("B" or "C")):
    print("windowless cabin above the car deck.")

else: print("Invalid cabin class")

print("\n3_3\n")

gender = input("What is your gender? (m/f): ")
hemoglobin = float(input("Enter your hemoglobin value here in g/l here: "))

if (gender == "f"):
    if ( hemoglobin >= 117 and hemoglobin <= 155):
        print("Your hemoglobin value is normal.")
    elif ( hemoglobin < 117 ):
        print("Your hemoglobin value is low.")
    else:
        print("Your hemoglobin value is high.")
elif (gender == "m"):
    if (hemoglobin >= 134 and hemoglobin <= 167):
        print("Your hemoglobin value is normal.")
    elif (hemoglobin < 134):
        print("Your hemoglobin value is low.")
    else:
        print("Your hemoglobin value is high.")
else:
    print("Invalid input")

print("\n3_4\n")

year = int(input("Enter a year: "))

if (year % 100 == 0 and year % 400 == 0):
    print(f"The year {year} is a leap year.")
elif (year % 4 == 0 and not year % 100 == 0):
    print(f"The year {year} is a leap year.")
else:
    print(f"The year {year} is not a leap year.")

