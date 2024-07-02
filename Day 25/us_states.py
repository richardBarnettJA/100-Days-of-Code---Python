import turtle
import pandas
from add_state import Add_State

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

file = "50_states.csv"
states = pandas.read_csv(file)
states_list = states["state"].to_list()

guessed_states = []

while len(guessed_states) < 50:
    guess_state = screen.textinput(title=f"{len(guessed_states)}/50 - Guess the State", prompt="What's another state's name?: ").title()
    if guess_state =="Exit":
        break
    elif guess_state in states_list:
        selected_state = states[states["state"] == guess_state]
        guessed_states.append(guess_state)
        x = int(selected_state.x)
        y = int(selected_state.y)
        Add_State(x, y, guess_state)
    else:
        print("State does not exist!")

missed_states = [x for x in states_list if x not in missed_states]


missed_states_dict = {
    "missed_states": missed_states
}

states_df = pandas.DataFrame(missed_states_dict)
states_df.to_csv("missed_states.csv")


# screen.exitonclick()