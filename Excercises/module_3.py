#3_1

ask = float(input("Enter the length of a zander you caught in cm: "))
short = 42-ask
if (ask >= 42):
    print(f"Congrats! You have caught a zander that is {ask} centimeter long.")
else:
    print(f"You need to release the fist back, it's {short} centimeter shot from the size limit.")

#3_2

cabinClass = input("Please enter the name of your class: ")
if (cabinClass == "LUX"):
    print("upper-deck cabin with a balcony.")
elif (cabinClass == "A"):
    print("above the car deck, equipped with a window.")
elif (cabinClass == ("B" or "C")):
    print("windowless cabin above the car deck.")

else: print("Invalid cabin class")

