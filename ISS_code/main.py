import requests
from datetime import datetime
import smtplib

MY_LAT = 42.238682 # Your latitude
MY_LONG = -87.959587 # Your longitude
MY_EMAIL ="pallaa15@gmail.com"
PASSWORD ="Enter your own passwordd"
RECIEVER= "pallaabhi45@gmail.com"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

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
hour_now =time_now.hour
#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

print(f"iss_latitude is currently at {iss_latitude}" )
print(f"iss_longitude is currently at {iss_longitude}")
print(f"hour_now is {hour_now}")
# print(data)
print(f"sunrise is {sunrise}")
print(f"sunset is {sunset}")
print(f"your latitude is {MY_LAT}")
print(f"Your longitude is {MY_LONG}")

if abs(iss_latitude - MY_LAT)<=5 and abs(iss_longitude - MY_LONG)<=5 and (hour_now <= 18 and hour_now <= 3):
    connection = smtplib.SMTP("smtp.gmail.com",587)
    connection.starttls()
    connection.login(user=MY_EMAIL, password=PASSWORD)
    connection.sendmail(from_addr=MY_EMAIL,to_addrs=RECIEVER,
                        msg="Subject:ISS is near by\n\n"
                            "Go out and take a look")





