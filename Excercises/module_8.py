print("<8_1>\n\n")

# Write a program that asks the user to enter the ICAO code of an airport.
# The program fetches and prints out the corresponding airport name
# and location (town) from the airport database used on this course.
# The ICAO codes are stored in the ident column of the airport table.

import mysql.connector

def getAirportnameByICAOcode (ident):
    sql = "SELECT name, municipality FROM airport WHERE airport.ident = '" + ident + "'"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            print(f"The ICAO code {ident} corresponds to {row[0]} and it is located in {row[1]}.")
        return


connection = mysql.connector.connect(
    host = '127.0.0.1',
    port = 3306,
    database = 'flight_game',
    user = 'root',
    password = 'hyonee',
    autocommit = True
)

ident = input("Enter a ICAO code: ")
getAirportnameByICAOcode(ident)

print("\n\n<8_2>\n\n")

# Write a program that asks the user to enter the area code (for example FI)
# and prints out the airports located in that country ordered by airport type.
# For example, Finland has 65 small airports, 15 helicopter airports and so on.

def getCountryAndTypeByIso_country(iso_country):
    sql = "SELECT airport.name, airport.type from country, airport WHERE country.iso_country = airport.iso_country AND airport.iso_country = '" + iso_country + "' ORDER BY airport.type"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount >0 :
        for row in result:
            print(f"The airport in area {iso_country}: {row[0]} and its type is {row[1]}.")
        return

iso_country = input("Enter an area code: ")
getCountryAndTypeByIso_country(iso_country)


print("\n\n<8_3>\n\n")

# Write a program that asks the user to enter the ICAO codes of two airports.
# The program prints out the distance between the two airports in kilometers.
# The calculation is based on the airport coordinates fetched from the database.
# Calculate the distance using the geopy library: https://geopy.readthedocs.io/en/stable/.
# Install the library by selecting View / Tool Windows / Python Packages in your PyCharm IDE,
# write geopy into the search field and finish the installation.

def calculateDistance(ident1,ident2):
    from geopy import distance

    sql1 = "SELECT latitude_deg, longitude_deg, name FROM airport WHERE ident = '" + ident1 + "'"
    print(sql1)
    cursor = connection.cursor()
    cursor.execute(sql1)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
           # print(f"The {row[2]} is located in ({row[0]},{row[1]}).")
            lo1 = (row[0],row[1])

    sql2 = "SELECT latitude_deg, longitude_deg, name FROM airport WHERE ident = '" + ident2 + "'"
    print(sql2)
    cursor = connection.cursor()
    cursor.execute(sql2)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
           # print(f"The {row[2]} is located in ({row[0]},{row[1]}).")
            lo2 =(row[0],row[1])
    distanceKm = distance.distance(lo1,lo2).km
    print(f"The distance between {ident1} and {ident2} is approx. {distanceKm:.3f} km.")



airport1 = input("Enter the first airport's ICAO code: ") # EFHK
airport2 = input("Enter the second airport's ICAO code: ") # RKSI

calculateDistance(airport1,airport2)