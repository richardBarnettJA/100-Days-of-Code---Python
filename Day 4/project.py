import random
print("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.")

num = input()

if num != "0" or num != "2" or num != "2":
    print("Invalid Input")
    exit

num = int(num)
cnum = random.randint(0, 2)
options = ["Rock", "Paper", "Scissors"]

if num == cnum:
    print("You both chose " + options[num])
    print("Draw!!!")
elif num == 0 and cnum == 1:
    print("You chose " + options[num])
    print("The computer chose " + options[cnum])
    print("You Lose")
elif num == 1 and cnum == 0:
    print("You chose " + options[num])
    print("The computer chose " + options[cnum])
    print("You Win")
elif num == 1 and cnum == 2:
    print("You chose " + options[num])
    print("The computer chose " + options[cnum])
    print("You Lose")
elif num == 2 and cnum == 1:
    print("You chose " + options[num])
    print("The computer chose " + options[cnum])
    print("You Win")
elif num == 2 and cnum == 0:
    print("You chose " + options[num])
    print("The computer chose " + options[cnum])
    print("You Lose")
elif num == 0 and cnum == 2:
    print("You chose " + options[num])
    print("The computer chose " + options[cnum])
    print("You Win")