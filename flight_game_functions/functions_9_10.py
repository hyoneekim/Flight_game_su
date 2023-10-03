import mysql.connector

connection = mysql.connector.connect(
    host = '127.0.0.1',
    port = 3306,
    database = 'flight_game_team12_mysql',
    user = 'root',
    password = 'hyonee',
    autocommit = True
)

def game_over(id):
    sql1 = f"SELECT player_name, total_travelled FROM player WHERE (co2_budget <= co2_consumed) AND (id = {id})"
    print(sql1)
    cursor = connection.cursor()
    cursor.execute(sql1)
    result = cursor.fetchall()
    if cursor.rowcount == 1:
        for row in result:
            print(f"{row[0]}, You cannot fly with the remaining budget anywhere. GAME OVER!")
        return

# for test
test1 = int(input("player id?: "))
game_over(test1)