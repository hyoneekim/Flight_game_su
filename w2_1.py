x = int(input("How  much cash you have?"))
answer = input("Can I check how much you got in your pocket? (y/n)")
#str = "You have {} cash"
#print(str.format(x))
print(f"You said that you have {x}.")
if (answer == "y"):
    if (x>1000):
        print("you have more than 1000 euros.")
    elif(x>10):
        print("You have more than 10 euros, but not as much as 1000 euros.")
    else:
        print("You poor thing...")
else:
    print("Noooooo why")