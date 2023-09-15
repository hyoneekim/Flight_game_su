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
