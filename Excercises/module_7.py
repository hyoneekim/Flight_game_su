print("<7_1>\n\n")

# Write a program that asks the user for a number of a month
# and then prints out the corresponding season (spring, summer, autumn, winter).
# Save the seasons as strings into a tuple in your program.
# We can define each season to last three months, December being the first month of winter.

seasons = ("spring", "summer", "autumn", "winter")
months = ("January", "February", "March", "April", "May", "June", "July", "August",
          "September", "October", "November", "December")


def month_to_season(x):
    month = months[x - 1]
    if (month in months[2:5]):
        return seasons[0]
    elif (month in months[5:8]):
        return seasons[1]
    elif (month in months[8:11]):
        return seasons[2]
    elif (month in months[0:2] or month == months[-1]):
        return seasons[3]

askMonth = int(input("Enter a number of a month (1-12): "))
print(f"{months[askMonth - 1]} is {month_to_season(askMonth)}.")

print("\n\n<7_2>\n\n")
#Write a program that asks the user to enter names until he/she enters an empty string.
#After each name is read the program either prints out New name or Existing name
# depending on whether the name was entered for the first time.
# Finally, the program lists out the input names one by one, one below another in any order.
# Use the set data structure to store the names.

names = {"Antti", "John"}

def is_name_in(x,y):
    if (x in y):
        print(f"The name '{x}' is already in the list.")
    else:
        y.add(x)
        print(f"The name '{x}' has been added.")


askName = input("Enter a name. Exit by hitting Enter key.: ")
while (askName != ""):
    is_name_in(askName, names)
    askName = input("Enter a name. Exit by hitting Enter key.: ")
if (askName == ""):
    print("The listed names are: \n")
    for x in names:
        print(x)

print("\n\n<7_3>\n\n")


