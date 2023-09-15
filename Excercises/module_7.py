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

names = set()

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
    print("\nYou chose to exit. \nThe listed names are: \n")
    for x in names:
        print(x)

print("\n\n<7_3>\n\n")
# Write a program for fetching and storing airport data.
# The program asks the user if they want to enter a new airport,
# fetch the information of an existing airport or quit.
# If the user chooses to enter a new airport,
# the program asks the user to enter the ICAO code and name of the airport.
# If the user chooses to fetch airport information instead,
# the program asks for the ICAO code of the airport and prints out the corresponding name.
# If the user chooses to quit, the program execution ends.
# The user can choose a new option as many times they want until they choose to quit.
# (The ICAO code is an identifier that is unique to each airport.
# For example, the ICAO code of Helsinki-Vantaa Airport is EFHK.
# You can easily find the ICAO codes of different airports online.)
airports = {
   "EFHK" : "Helsinki-Vantaa"
}
processing = True

def add_airport (y):
   ICAO = input("\nEnter the ICAO code of a new airport. : ")
   name = input("\nWhat is the name of the new airport? : ")
   if (ICAO not in y):
      airports[ICAO] = name
      print("\nThe New airport has been added.")
   else:
      print("\nThe airport is already in the database.")

def fetch_airport (y):
   ICAO = input("\nEnter the ICAO code of an airport to fetch its data. : ")
   if( ICAO in y):
      print(f"\nName found: The name for code {ICAO} is {airports[ICAO]} airport.")
   else:
      print("\nThe code not found or incorrect input.")


while processing:
   print("\n\n1: Enter a new airport")
   print("2: Fetch information of an existing airport")
   print("3: Quit\n\n")

   askCommand = int(input("Enter a number of your command. : "))
   if (askCommand == 1):
      add_airport(airports)
   elif (askCommand == 2):
      fetch_airport(airports)
   elif (askCommand ==3):
      processing = False
      print("Goodbye.")
   else:
      print("\nInvalid input. Please enter again.")