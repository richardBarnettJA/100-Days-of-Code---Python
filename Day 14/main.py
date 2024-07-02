# Higher or Lower Game

from game_data import data
from art import logo, vs
import random
import os

def get_info(choice):
    return choice["name"], choice["description"], choice["country"]


def display(choiceA, choiceB, counter):
    """Takes both choices and displays the options to the user. Also asks for which option
    they would like to choose then returns the response. Also shows the game counter"""
    print(logo)
    if counter > 0:
        print(f"You're right! Current score: {counter}.")
    name, description, country = get_info(choiceA)
    print(f"Compare A: {name}, a {description}, from {country}.")
    print(vs)
    name, description, country = get_info(choiceB)
    print(f"Against B: {name}, a {description}, from {country}.")
    return (input("Who has more followers? Type 'A' or 'B': ")).lower()

def get_choices(choice2):
    """This functions is used to return the randomly selected choices from the 
    data set. Takes choice2 to see if choice1 should be derived or set as choice2.
    """
    if choice2 == "":
        choice1 = random.choice(data)
    else:
        choice1 = choice2
    same = True
    while same:
        choice2 = random.choice(data)
        if choice1 != choice2:
            same = False
    return choice1, choice2

def check_winner(response, choice1, choice2):
    """This function takes the user's response and both choices to see if they have gotten the answer
    correct or not to see if the game should stop or not"""
    if response == "a":
        if choice1["follower_count"] >= choice2["follower_count"]:
            return True
        else:
            return False
    elif response == "b":
        if choice2["follower_count"] >= choice1["follower_count"]:
            return True
        else:
            return False
    else:
        return False
    
def game_over(counter):
    """This function prints the counter and game over message when the user loses."""
    print(logo)
    print(f"Sorry, that's wrong. Final score: {counter}")


def game():
    is_game = True
    choice2 = ""
    counter = 0
    while is_game:
        os.system("cls")
        choice1, choice2 = get_choices(choice2)       
        response = display(choice1, choice2, counter)
        is_game = check_winner(response, choice1, choice2)
        if is_game:
            counter += 1
    os.system("cls")
    game_over(counter)
        
game()
