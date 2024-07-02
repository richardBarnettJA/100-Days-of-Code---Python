#Rules of Blackjack
# Players are handed two cards initially and each card has a specific
# Number associated with it. The goal is to get your total sum in cards
# to 21 or as close to it with 21 being the ceiling. If you go over it, you instantly lose.
# This is a 2 player game where the closest player to 21 wins. You can ask for more cards 
# if you beleive that the card will help you get closer to 21.

import random
from art import logo
import os


def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def check_11(cards):
    """Takes cards and checks to see if the card 11 should be changed to a 1"""
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return cards

def check_bust(user, computer):
    """Checks to see if there is a winner"""
    if sum(user) > 21:
        results(user, computer)
        if sum(computer) > 21:
            print("You both went Bust! You both lose!!! 🙃")
            return "n"
        else:
            print("You went Bust! You lose!!! 😭")
            return "n"
    elif sum(computer) > 21:
        results(user, computer)
        print("Computer went Bust! You Win!!! 😁")
        return "n"
    else:
        return "y"
    
def check_blackjack(user, computer):
    """Takes user and computer cards to check if there is a blackjack"""
    if sum(user) == 21 or sum(computer) == 21:
        results(user, computer)
        if sum(user) == 21 and sum(computer) == 21:
            print("You both have Blackjack! Draw! 🙃")
        elif sum(user) == 21:
            print("You have Blackjack! You have Won!!! 😎")
        elif sum(computer) == 21:
            print("The computer has Blackjack! You have lost! 😤")
        return "n"
    return "y"
    
def check_winner(user, computer):
    """Takes user and computer cards to check if there is a winner"""
    if sum(user) > sum(computer):
        print("You win!!! 😃")
    elif sum(user) == sum(computer):
        print("Draw! 🙃")
    else:
        print("You lose!!! 😤")
    
def results(user, computer):
    """Takes the user and computer cards in order to display final results"""
    print(f"Your final hand: {user}, final score: {sum(user)}")
    print(f"Computer's final hand: {computer}, final score: {sum(computer)}")


def game():
    os.system("cls")
    play = "y"
    while play == "y":
        play = (input("Do you want to play a game of Blackjack? Type 'y' for YES or 'n' for NO: ")).lower()
        if play == "y":
            os.system("cls")
            print(logo)
            user_deck = []
            computer_deck = []
            for x in range(2):
                user_deck.append(deal_card())
            while sum(computer_deck) < 17:
                computer_deck.append(deal_card())
                computer_deck = check_11(computer_deck)
            another = "y"
            while another == "y":
                another = check_blackjack(user_deck, computer_deck)
                if another == "y":
                    user_deck = check_11(user_deck)
                    another = check_bust(user_deck, computer_deck)
                if another == "y":
                    print(f"Your cards: {user_deck}, current score: {sum(user_deck)}")
                    print(f"Computer's first card: {computer_deck[0]}")
                    another = (input(" Type 'y' to get another card, type 'n' to pass: ")).lower()
                    if another == "y":
                        user_deck.append(deal_card())
                    else:
                        results(user_deck, computer_deck)
                        check_winner(user_deck, computer_deck)
    print("Goodbye!!!")


game()
