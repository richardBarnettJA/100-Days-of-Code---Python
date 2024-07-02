# Layouts
# Pack, place, grid
# place(x=0, y=100)
from tkinter import *

def button_click():
    print("I got clicked")
    my_label.config(text="I Got Clicked")
    print(input.get())

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)


# Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.grid(column=1, row=1)

my_label["text"] = "New Text"
my_label.config(text="New Text")


# Button
button = Button(text="Click Me", command=button_click)
button.grid(column=2, row=2)



# Entry
input = Entry(width=50, )
input.grid(column=3, row=3)
input.insert(END, string="Email")



window.mainloop()