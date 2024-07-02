from tkinter import *
import pandas as pd
import random as rd


BACKGROUND_COLOR = "#B1DDC6"
CARD_BACK = "./images/card_back.png"
CARD_FRONT = "./images/card_front.png"
RIGHT = "./images/right.png"
WRONG = "./images/wrong.png"
FONT1 = ("Arial", 40, "italic")
FONT2 = ("Arial", 60, "bold")
CSV = "./data/french_words.csv"
word_dict = {}
SAVE_CSV = "./data/words_to_learn.csv"



# Read From CSV
try:
    data = pd.read_csv(SAVE_CSV)
except FileNotFoundError:
    data = pd.read_csv(CSV)
finally:
    data_dict = data.to_dict(orient="records")
# print(data_dict)


# Flip Card Function
def flip_card():
    global word_dict
    canvas.itemconfig(card_image, image=card_back)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_text, text=word_dict["English"], fill="white")




# Random Word From Button Click

def next_word():
    global flip_timer, word_dict
    screen.after_cancel(flip_timer)
    canvas.itemconfig(card_image, image=card_front)
    new_word = rd.choice(data_dict)
    word_dict = new_word
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_text, text=new_word["French"], fill="black")
    flip_timer = screen.after(3000, flip_card)



def right_answer():
    global word_dict
    data_dict.remove(word_dict)
    df = pd.DataFrame(data_dict)
    df.to_csv(SAVE_CSV, index=False)
    next_word()






# UI

# Window Setup
screen = Tk()
screen.config(padx=50, pady=50, bg=BACKGROUND_COLOR, width=800, height=526)
flip_timer = screen.after(3000, flip_card)



# Card Image Setup (Canvas)
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_back = PhotoImage(file=CARD_BACK)
card_front = PhotoImage(file=CARD_FRONT)
card_image = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 150, text="Title", font=FONT1)
card_text = canvas.create_text(400, 265, text="Word", font=FONT2)
canvas.grid(row=0, column=0, columnspan=2)




# Buttons
wrong_image = PhotoImage(file=WRONG)
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_word)
wrong_button.grid(row=1, column=0)


right_image = PhotoImage(file=RIGHT)
right_button = Button(image=right_image, highlightthickness=0, command=right_answer)
right_button.grid(row=1, column=1)










next_word()  #Call function so new word is populated as the program starts


screen.mainloop()