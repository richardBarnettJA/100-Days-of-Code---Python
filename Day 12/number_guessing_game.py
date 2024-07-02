#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
from art import logo
import os


EASY = 10
HARD = 5


def check_match(goal, guess, tries):
    if goal == guess:
        print(f"You got it! The answer was {goal}")
        return False
    elif goal > guess:
        print("Too low")
        if tries > 1:
            print("Guess Again")
        return True
    else:
        print("Too high")
        if tries > 1:
            print("Guess Again")
        return True


def game():
    os.system("cls")
    target = random.randint(1, 100)

    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = (input("Choose a diffiulty. type 'easy' or 'hard': ")).lower()
    tries = 0
    if difficulty == "easy":
        tries = EASY
    elif difficulty == "hard":
        tries = HARD
    is_playing = True
    while tries > 0 and is_playing == True:
        print(f"You have {tries} attemps remaining to guess the number.")
        guess = int(input("Make a guess: "))
        is_playing = check_match(target, guess, tries)
        tries -= 1
    if is_playing:
        print("You've run out of guesses, you lose.")



game()