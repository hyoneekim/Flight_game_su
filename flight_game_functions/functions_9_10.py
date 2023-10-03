import mysql.connector

connection = mysql.connector.connect(
    host = '127.0.0.1',
    port = 3306,
    database = 'flight_game_team12_mysql',
    user = 'root',
    password = 'hyonee',
    autocommit = True
)

# weak logic. need to improve later on.
def game_over_and_save(id):
    global name, score
    sql1 = f"SELECT player_name, total_travelled FROM player WHERE (co2_budget <= co2_consumed) AND (id = {id})"
    print(sql1)
    cursor = connection.cursor()
    cursor.execute(sql1)
    result = cursor.fetchall()
    if cursor.rowcount == 1:
        for row in result:
            print(f"{row[0]}, You cannot fly with the remaining budget anywhere. GAME OVER!")
            name = row[0]
            score = row[1]
    save = input("Do you want to save your score in the score board? (y/n): ")
    if save == 'y':
        sql2 = f"INSERT INTO scoreboard (player_name, score) VALUES (%s, %s)"
        val = [name, score]
        cursor = connection.cursor()
        cursor.execute(sql2, val)
        print(f"your userid <{name}> and your score <{score}> has been updated to the scoreboard.")
    return

def show_scoreboard():
    sql = "SELECT * FROM scoreboard ORDER BY score DESC LIMIT 50"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        print(f"Player      | score")
        print(f"--------------------------")
        for row in result:
            print(f"{row[1]} | {row[2]}")
        return

# only for test. needs to be change later on when merging all the functions.
test1 = int(input("player id?: "))
game_over_and_save(test1)

exit_process = True

while exit_process:
    toScoreboard = input("Do you want to go check scoreboard? (y/n) : ")
    if toScoreboard == 'y':
        show_scoreboard()
        exit_process = False
    elif toScoreboard == 'n':
        print("Bye bye!")
        exit_process = False
    else:
        print("Invalid answer. Try again.")
