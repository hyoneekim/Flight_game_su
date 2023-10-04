import mysql.connector

connection = mysql.connector.connect(
    host = '127.0.0.1',
    port = 3306,
    database = 'flight_game_team12_mysql',
    user = 'root',
    password = 'hyonee',
    autocommit = True
)


def condition_checker(userid):
    global co2_budget, co2_consumed

    sql = f"SELECT co2_budget, co2_consumed FROM player WHERE player_name = '{userid}'"

    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount == 1:
        for row in result:
            co2_budget = row[0]
            co2_consumed = row[1]
    co2_left = co2_budget - co2_consumed
    if co2_left <= 0:

        return game_over_and_save(userid)
    else:
        return
    # weak logic. need to improve later on.
def game_over_and_save(userid):
    global name, score
    sql1 = f"SELECT player_name, total_travelled FROM player WHERE (co2_budget <= co2_consumed) AND (player_name = '{userid}')"
    #print(sql1)
    cursor = connection.cursor()
    cursor.execute(sql1)
    result = cursor.fetchall()
    if cursor.rowcount == 1:
        for row in result:
            print(f"{row[0]}, You cannot fly with the remaining budget anywhere. GAME OVER!")
            name = row[0]
            score = row[1]
    save = input("Do you want to save your score in score board? (y/n): ")
    if save == 'y':
        sql2 = f"INSERT INTO scoreboard (player_name, score) VALUES (%s, %s)"
        val = [name, score]
        cursor = connection.cursor()
        cursor.execute(sql2, val)
        print(f"your userid <{name}> and your score <{score}> has been saved in the scoreboard.")
    return

def show_scoreboard():
    sql = "SELECT * FROM scoreboard ORDER BY score DESC LIMIT 50"
    #print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        print(f"<<<SCORE BOARD>>>")
        print(f"Player      | score")
        print(f"--------------------------")
        for row in result:
            print(f"{row[1]} | {row[2]}")
        return

# FRONT END(ish) FUNCTIONS & CODES START HERE-------------------
def main_display(userid):
    sql1 = f"SELECT COUNT(player_id) FROM choice WHERE player_id = '{userid}'"
    cursor = connection.cursor()
    cursor.execute(sql1)
    result = cursor.fetchall()
    if cursor.rowcount == 1:
        for row in result:
            print(f"ROUND {row[0]}.")
            print("\n")

    sql2 = f"SELECT co2_budget, co2_consumed, total_travelled FROM player where player_name = '{userid}'"
    cursor = connection.cursor()
    cursor.execute(sql2)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            print("<<Your status>>")
            print("-------------------------------------")
            print(f"|co2_budget              | {row[0]}|")
            print(f"|co2_consumed            | {row[1]}|")
            print(f"|total distance travelled| {row[2]}|")
            print("-------------------------------------")
    return

def front_display():
    initial = True
    while initial:
        print("----------------------")
        print("|  NAME OF THE GAME  |")
        print("|                    |")
        print("----------------------")
        print("\n")
        print("1: START A NEW GAME")
        print("2: CHECK TUTORIAL")
        print("3: SCORE BOARD")
        print("4: QUIT")
        print("\n")

        command = int(input("Enter your command: "))
        if command == 1:
            test1 = input("player id?: ")  # assuming that the game goes on and reached to this phase.
            # connects to creating userid def. for now, I'm using what I have (game over function -> the end)
            print(f"Welcome traveller, {test1}! ")
            main_display(test1)
            game_over_and_save(test1)
            initial = False

        elif command == 2:
            print("<<TUTORIAL>>")
            print("\n")
            print("You're going to travel across the world by choosing a flight.")
            print("Your GOAL is to travel as far as you can go with your limited co2 budget!")
            print("The game ends when you have spent all the budget and can't go anywhere anymore.")
            print("Good luck!")
            print("\n")
            print("Going back to the front page...")
            print("\n")

        elif command == 3:
            show_scoreboard()
            print("\n")
            print("Going back to the front page....")
            print("\n")
            print("\n")
        elif command == 4:
            print("Bye bye!")
            initial = False
        else:
            print("Invalid command. Please try again!")





# only for test. needs to be change later on when merging all the functions.
front_display()



exit_process = True

while exit_process:
    toScoreboard = input("Do you want to go check score board? (y/n) : ")
    if toScoreboard == 'y':
        show_scoreboard()
        toFrontPage = input("By hitting enter, you'll go back to the front page.: ")
        if toFrontPage == '':
            front_display()
        exit_process = False
    elif toScoreboard == 'n':
        toFrontPage = input("By hitting enter, you'll go back to the front page.: ")
        if toFrontPage == '':
            front_display()
        exit_process = False
    else:
        print("Invalid answer. Try again.")
