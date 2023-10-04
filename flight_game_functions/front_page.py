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
            # connects to creating userid def
            initial = False
        elif command == 2:
            # bring the tutorial & come back to this page (from another file if possible?)
            return
        elif command == 3:
            # show_scoreboard() & come back to this page
            return
        elif command == 4:
            print("Bye bye!")
            initial = False
        else:
            print("Invalid command. Please try again!")

front_display()


