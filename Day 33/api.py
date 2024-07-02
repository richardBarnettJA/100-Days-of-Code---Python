import requests
from datetime import datetime
import smtplib
from time import sleep


# 1XX - Hold on
# 2XX - Here You Go
# 3XX - Go Away
# 4XX - You Screwed Up
# 5XX - I Screwed Up (The Server might be down)

# 200 - Success
# 404 - does not exists/not FileNotFoundError

MY_LAT = 18.069962
MY_LONG = -76.814014
MY_EMAIL = "rbarnetttestemail@gmail.com"
MY_PASSWORD = "jwcebctsldhojxhe"
PORT = 587
SMTP_SERVER = "smtp.gmail.com"
TO_EMAIL = "campion1boy@gmail.com"



def is_close(lat, long, sr, ss, tn):
    if lat-5 <= MY_LAT <= lat+5:
        if long-5 <= MY_LONG <= long+5:
            if tn < sr or tn > ss:
                return True
    return False


while True:
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    # print(response)
    # print(response.status_code)

    response.raise_for_status() #raises an exception if not 200

    data = response.json()
    # print(data)
    longitude = float(data["iss_position"]["longitude"])
    latitude = float(data["iss_position"]["latitude"])
    iss_position = (latitude, longitude)
    # print(iss_position)


    # APIs that require paramters

    parameters = {
        "lat" : MY_LAT,
        "lng" : MY_LONG,
        "formatted": 0
    }

    # Could also do it like this 
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = data["results"]["sunrise"]
    sunset = data["results"]["sunset"]
    # print(sunrise)

    sunrise_hour = int(sunrise.split("T")[1].split(":")[0])
    sunset_hour = int(sunset.split("T")[1].split(":")[0])


    time_now = datetime.now()
    now_hour = time_now.hour

    result = is_close(latitude, longitude, sunrise_hour, sunset_hour, now_hour)
    if result:
        with smtplib.SMTP(SMTP_SERVER, PORT) as conenction:
            conenction.starttls()
            conenction.login(user=MY_EMAIL, password=MY_PASSWORD)
            conenction.sendmail(from_addr=MY_EMAIL, to_addrs=TO_EMAIL, msg="Subject:Look Up!\n\nLook up! The International Space Station Is Currently Flying Above You!")
        print("Email Sent!")
    else:
        print(f"Not In Range! \nSpace Station location: {iss_position}, \nYour Position: {(MY_LAT, MY_LONG)}")
    print("-----------------------------------------------")
    sleep(60)
