print("Welcome to Treasure Island")
print("Your mission is find treasure")
choice1 = input("You're at a crossroad, where do you want to go? Type \"left\" or \"right\". ").lower()
if choice1 == "left":
    choice2 = input("You've come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat or type \"swim\" to swim across. ").lower()
    if choice2 == "wait":
        choice3 = input("You arrive at the island anharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? ").lower()
        if choice3 == "red":
            print("It's a room full of fire. game Over!")
        elif choice3 == "yellow":
            print("You found the treasure! You Win!")
        elif choice3 == "blue":
            print("You entered a room of beasts. Game Over!")
        else: 
            print("You chose a room that doesn't exist. game Over!")
    else:
        print("You got attacked by an angry trout. Game Over!")
else:
    print("You fell into a hole. Game Over!")