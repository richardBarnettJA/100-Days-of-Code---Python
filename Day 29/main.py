from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


FILE = "password_manager_data.json"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Modified version from DAY 5 project.py
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters= random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    
    password_list = []
    [password_list.append(random.choice(letters)) for x in range(nr_letters)]
    [password_list.append(random.choice(symbols)) for x in range(nr_symbols)]
    [password_list.append(random.choice(numbers)) for x in range(nr_numbers)]


    random.shuffle(password_list)
    password = ''.join(password_list)
    add_password(password)


def add_password(password):
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def get_data():
    website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()
    if not website or website.isspace():
        messagebox.showwarning(title="Missing Website", message="You did not enter a website.\nPlease try again and enter a valid website.")
    elif not email or email.isspace():
        messagebox.showwarning(title="Missing Email/Username", message="You did not enter a email/username.\nPlease try again and enter a valid email/username.")
    elif not password or password.isspace():
        messagebox.showwarning(title="Missing Password", message="You did not enter a password.\nPlease try again and enter a valid password.")
    else:  
        add_to_file(website, email, password)
        clear_fields()
    

def clear_fields():
    website_entry.delete(0, END) #Start index and end index in which to be deleted
    password_entry.delete(0, END)


def add_to_file(website, email, password):
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    try:
        with open(FILE, "r") as f:
            # json.dump(new_data, f, indent=4)
            data = json.load(f)  # Stores the data as a python dictionary
            data.update(new_data)
            new_data = data
    except:
        print("File Not Found")
    finally:
        with open(FILE, "w") as f:
            json.dump(new_data, f, indent=4)
    print("Password added successfully")
    success_label.config(text="Password added successfully")



# ---------------------------- Search Information ------------------------------- #

def search_password():
    website = website_entry.get()
    try:
        with open(FILE, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:  
        is_found = False  
        for (key, value) in data.items():
            if website.lower() == key.lower():
                is_found = True
                email = value["email"]
                password = value["password"]
                messagebox.showinfo(title=key, message=f"Email: {email}\nPassword: {password}")
        if not is_found:
            messagebox.showinfo(title="Error", message=f"No Website named '{website}' Found.") 




# ---------------------------- UI SETUP ------------------------------- #

screen = Tk()
screen.title("Password Manager")
screen.config(padx=50, pady=50)
logo = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_username_label = Label(text="Email/Username:")
email_username_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

success_label = Label(text="", fg="#00FF00")
success_label.grid(row=5, column=1)


# Entries
website_entry = Entry(width=33)
website_entry.focus()
website_entry.grid(row=1, column=1)

email_username_entry = Entry(width=52)
email_username_entry.insert(0, "email@gmail.com") #0 is the index of where it will be inserted. You could use END to insert at the end.
email_username_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry(width=33)
password_entry.grid(row=3, column=1)


# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(width=44, text="Add", command=get_data)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search", command=search_password, width=15)
search_button.grid(row=1, column=2)








screen.mainloop()