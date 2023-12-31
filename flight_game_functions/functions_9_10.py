import mysql.connector

connection = mysql.connector.connect(
    host = '127.0.0.1',
    port = 3306,
    database = 'flight_game_team12_mysql',
    user = 'root',
    password = 'hyonee',
    autocommit = True
)

# BACKEND functions start here ----------------
def get_airport_info(icao):
    sql = f'''SELECT iso_country, ident, name, latitude_deg, longitude_deg
                  FROM airport
                  WHERE ident = %s'''
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql, (icao,))
    result = cursor.fetchone()
    return result


def calculate_distance(current, target):
    from geopy import distance

    start = get_airport_info(current)
    end = get_airport_info(target)
    return distance.distance((start['latitude_deg'], start['longitude_deg']),
                             (end['latitude_deg'], end['longitude_deg'])).km

def get_userdata(userid):
    sql = f'''SELECT player_name, co2_budget, co2_consumed, total_travelled FROM player WHERE player_name = %s
                '''
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql, (userid,))
    result = cursor.fetchone()
    return result

def left_budget(userid):
    data = get_userdata(userid)
    return data['co2_budget'] - data['co2_consumed']

def range_in (airplane_size, userid):
    global airportCode, range, co2_emission
    current = input("Type the code of your current location: ")

    sql = f'''SELECT ident, airport.name, airport.continent, country.name as country, airplane.max_range, airplane.co2_emission_per_km, airplane.capacity
            FROM airport 
            INNER JOIN airplane on (airplane.size = airport.type)
            INNER JOIN country on (airport.iso_country = country.iso_country)
            WHERE airport.type = '{airplane_size}' ORDER BY RAND () LIMIT 5'''
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    print("\nHere are possible destinations you can choose!\n")
    print("continent |  country  |  airport  |  distance  | expected co2 emission")
    print("-----------------------------------------")
    if cursor.rowcount >0:
        for row in result:
            #print(f"{row[0]}")
            airportCode = row[0]
            range = row[4]
            distance = calculate_distance(current, airportCode)
            co2_emission = distance * row[4]/ row[5]

            if (range > distance) and (co2_emission < left_budget(userid)):
                print(f"    {row[2]}    | {row[3]} | {row[1]} | {round(distance)} km | {round(co2_emission)}")
                # NEED TO ADD: IF THERE ISN'T ANY RESULT SHOWN HERE, REDIRECT THE PLAYER TO CHOOSE SMALLER PLANE?
                # AFTER PLANE SELECTION HAS BEEN DONE.

    return

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

def show_panel(userid):
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

# FRONT END(ish) FUNCTIONS & CODES START HERE-------------------
def main_display(userid):
    main_processing = True
    while main_processing:
        sql1 = f"SELECT COUNT(player_id) FROM choice WHERE player_id = '{userid}'"
        cursor = connection.cursor()
        cursor.execute(sql1)
        result = cursor.fetchall()
        if cursor.rowcount == 1:
            for row in result:
                print(f"ROUND {row[0]+1}")
                print("\n")

        show_panel(userid)

        size = input("Type size of the plane you choose: ")
        condition_checker(userid)
        range_in(size,userid)
        main_processing = False

    print("\n\n from here continue : ask the player his/her decision and double check=--------`...")
    print("\n\n up in the air...")
    print("\n\n 'you've got a message from control tower!' (If event occurs)")
    print("\n\n calculate the final co2_spent and update the data to choice table")
    print("\n\n 'Now it's landing....")

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
            test1 = input("player_name?: ")  # assuming that the game goes on and reached to this phase.
            # connects to creating userid def. for now, I'm using what I have (game over function -> the end)
            print(f"\nWelcome traveller, {test1}! ")
            main_display(test1)
            condition_checker(test1)
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
