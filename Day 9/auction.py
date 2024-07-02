from art import logo
import os

print(logo)
print("Welcome to the secret auction program.")
temp = True
auction = {}
while temp:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    auction[name] = bid
    more = (input("Are there any other bidders? Type 'yes' or 'no. ")).lower()
    if more == "no":
        temp = False
    os.system("cls")

temp2 = 0
winner = ""
for x in auction:
    if auction[x] > temp2:
        temp2 = auction[x]
        winner = x

print(f"The winner is {winner} with a bid of ${auction[winner]}.00.")