import random
import hangman_words
import hangman_art
import os



word_list = ["helper", "beekeeper", "honey", "chaser", "money"]

lives = 6

word = random.choice(hangman_words.word_list)
print(word)
guessed = []
guess_word = []
for x in word:
    guess_word.append("_")


while ("_" in guess_word):
    print(hangman_art.logo)
    print(hangman_art.stages[lives])
    print(guess_word)
    letter = (input("Please enter a letter to search for: ")).lower()
    if letter in guessed:
       os.system("cls")
       print("Letter has already been tried. Please try again.")
       continue
    guessed.append(letter)
    if letter not in word:
      os.system("cls")
      print(f"You guess {letter}. That is not in the word. You lose a life.")
      lives -= 1
      if lives == 0:
        print("You lost")
        break
      continue
    else:
      for x in range(len(word)):
          if word[x] == letter:
              guess_word[x] = letter
    os.system("cls")
else:
    print("You won")