import requests
from datetime import datetime
import smtplib

MY_EMAIL= "emailid"
PASSWORD= "password"


MY_LAT =  # Your latitude
MY_LONG = # Your longitude

def is_iss_close():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    #Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True



parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,

}
def is_dark():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    if sunrise >= time_now >= sunset:
        return True
while True:
  time.sleep(60)
  if is_iss_close() and is_dark():
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=MY_EMAIL, password=PASSWORD)
    connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg="SUBJECT: ISS is Close\n\n Hey, ISS is near to your location please come outside to watch it\n\n Enjoy!" )
    connection.close()




