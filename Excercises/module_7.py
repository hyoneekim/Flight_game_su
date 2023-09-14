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