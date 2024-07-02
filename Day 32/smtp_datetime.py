# import smtplib

# # SMTP INFORMATION
# # GMAIL = smtp.gmail.com
# # HOTMAIL = smtp.live.com
# # YAHOO = smtp.mail.yahoo.com

# my_email = "rbarnetttestemail@gmail.com"
# password = "jwcebctsldhojxhe"  #app password from my gmail security settings

# smtp_server = "smtp.gmail.com"
# port = 587  # or 465
# with smtplib.SMTP(smtp_server, port) as connection: #conenct to gmail server

#     connection.starttls() #TLS - transport layer security (encrypts data and secures the line)

#     connection.login(user=my_email, password=password)

#     connection.sendmail(from_addr=my_email, to_addrs="campion1boy@gmail.com", msg="Subject:Hello\n\nThis is the body of my email.")



# import datetime as dt

# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday() # 0 - Monday
# print(day_of_week)


# date_birth = dt.datetime(year=2002 , month=5 , day=30, hour=4)
# print(date_birth)



import datetime as dt
import smtplib
import random

now = dt.datetime.now()
if now.weekday() == 6:
    with open("./quotes.txt") as f:
        quotes = f.readlines()
        quote = random.choice(quotes)

    my_email = "rbarnetttestemail@gmail.com"
    password = "jwcebctsldhojxhe"
    port = 587
    smtp_server = "smtp.gmail.com"


    with smtplib.SMTP(smtp_server, port) as conenction:
        conenction.starttls()
        conenction.login(user=my_email, password=password)
        conenction.sendmail(from_addr=my_email, to_addrs="campion1boy@gmail.com", msg=f"Subject: Monday Motivational Quote\n\n{quote}")


    print("Email has been sent.")
else:
    print("It is not Modnay!")
    


