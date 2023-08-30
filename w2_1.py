print("a")
print("b")
print("c")

x = int(input("How  much cash you have?"))
#str = "You have {} cash"
#print(str.format(x))
print(f"You said that you have {x}.")

if (x>10):
    print("you have more than 10 euros.")
    if ( x>100000):
        print("You rich bastard")
else:
    print("You poor thing...")