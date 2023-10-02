import mysql.connector

connection = mysql.connector.connect(
    host = '127.0.0.1',
    port = 3306,
    database = 'flight_game_team12_mysql',
    user = 'root',
    password = 'hyonee',
    autocommit = True
)

def game_over(co2):
    sql = "SELECT co2_budget, co2_consumed FROM player WHERE co2_budget < co2_consumed '" + co2 + "'"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            print(f"You cannot fly with the left budget {row[0]-row[1]}. GAME OVER!")
        return

