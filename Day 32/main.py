##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.



import datetime as dt
import smtplib
import random
import pandas as pd



def generate_letter(name):
    num = random.randint(1, 3)
    file = f"./letter_templates/letter_{num}.txt"
    with open(file) as f:
        data = f.readlines()
    new_head = [data[0].replace("[NAME]", name)]
    return new_head + data[1:]


birthdays_csv = "./birthdays.csv"
birthdays = pd.read_csv(birthdays_csv)
birthdays_dict = birthdays.to_dict(orient="records")


my_email = "rbarnetttestemail@gmail.com"
password = "jwcebctsldhojxhe"
port = 587
smtp_server = "smtp.gmail.com"


now = dt.datetime.now()
month = now.month
day = now.day


is_sent = False
for bday in birthdays_dict:
    if bday["month"] == month and bday["day"] == day:
        address = bday["email"]
        name = bday["name"]
        letter = generate_letter(name)
        letter_str = " ".join(letter)
        with smtplib.SMTP(smtp_server, port) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=address, msg=f"Subject:Happy Birthday {name}!!!\n\n{letter_str}")
        print(f"Email sent to {name}.")
        is_sent = True

if not is_sent:
    print("There are no birthdays today!")



