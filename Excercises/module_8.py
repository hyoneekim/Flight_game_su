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

