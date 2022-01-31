import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 9.074410 # Your latitude
MY_LONG = -79.448810 # Your longitude

def send_mail():
    my_email = "jtitech.pty@gmail.com"
    password = "My_Password"

    with smtplib.SMTP("smtp.gmail.com") as conection:
        conection.starttls()
        conection.login(user=my_email, password=password)
        conection.sendmail(from_addr=my_email, to_addrs="jonathanlop82@gmail.com",
                           msg=f"Subject:It is near\n\nLook up.")

while True:
    time.sleep(60)
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    print(iss_latitude)
    print(iss_longitude)

    #Your position is within +5 or -5 degrees of the ISS position.


    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()

    #If the ISS is close to my current position

    if (iss_latitude >= (MY_LAT - 5) and iss_latitude <= (MY_LAT + 5)) and (iss_longitude >= (MY_LONG - 5) and iss_longitude <= (MY_LONG + 5) ):
       if time_now.hour >= sunset or time_now.hour <= sunrise:
           send_mail()
    else:
        print("It's away")




