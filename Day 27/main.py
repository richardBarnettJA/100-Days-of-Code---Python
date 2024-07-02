# GUI
from tkinter import *

def button_click():
    print("I got clicked")
    my_label.config(text="I Got Clicked")
    print(input.get())

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)


# Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.pack()

my_label["text"] = "New Text"
my_label.config(text="New Text")


# Button
button = Button(text="Click Me", command=button_click)
button.pack()


# Entry
input = Entry(width=50, )
input.pack()
input.insert(END, string="Email")


# textbox
# text = Text(height=5, width=30)
# text.focus() #Puts cursor in text box
# text.insert(END, "Multi-Line text entry example here!")
# print(text.get("1.0", END))  #1.0 means the firt line (1) starting at the charcter zero (0)
# text.pack()


# # Spinbox
# def spinbox_used():
#     print(spinbox.get())

# spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
# spinbox.pack()


# # Scale
# def scale_used(value):
#     print(value)

# scale = Scale(from_=0, to=100, command=scale_used)
# scale.pack()


# # Checkbutton
# def checkbutton_used():
#     print(checked_state.get())

# checked_state = IntVar()
# checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
# checked_state.get()
# checkbutton.pack()


# # Radiobutton
# def radio_used():
#     print(radio_state.get())

# radio_state = IntVar()
# radiobutton1 = Radiobutton(text="Option1", value=1,  variable=radio_state, command=radio_used)
# radiobutton2 = Radiobutton(text="Option2", value=2,  variable=radio_state, command=radio_used)
# radiobutton1.pack()
# radiobutton2.pack()


# # Listbox
# def listbox_used(event):
#     print(listbox.get(listbox.curselection()))

# listbox = Listbox(height=4)
# fruits = ["Apple", "Mango", "Guava", "Plum"]
# for item in fruits:
#     listbox.insert(fruits.index(item), item)
# listbox.bind("<<ListboxSelect>>", listbox_used)
# listbox.pack()








window.mainloop()