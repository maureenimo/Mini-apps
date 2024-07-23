import requests
import datetime as dt
from smtplib import SMTP
import time
# VARIABLES 
MY_LAT = 10.023559
MY_LONG = 37.906193

# Email variables
my_email = "pythonmaster56@gmail.com"
my_pass = "jqgu ardd vyfe nkpv"

# iss overheard
def position_overhead():
    res = requests.get("http://api.open-notify.org/iss-now.json")
    res.raise_for_status()
    data = res.json()
    
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG-5 <= iss_longitude <= MY_LONG +5:
        return True
    
# sunset/sunrise
def is_night():
    res = requests.get("https://api.sunrise-sunset.org/json?lat=MY_LAT&lng=MY_LONG&formatted=0")
    
    res.raise_for_status()
    data = res.json()
    sunrise_data= int[data["results"]["sunrise"].split("T")[1].split(":")[0]]
    sunset_data= int[data["results"]["sunset"].split("T")[1].split(":")[0]]
        
    # current day
    today = dt.datetime.now()
    hour = today.hour
    
    if hour >= sunset_data or hour <= sunrise_data:
        return True
        
# send mail
while True:
    time.sleep(60)
    if position_overhead() and is_night():
        with SMTP('smtp.gmail.com') as conn:
            conn.starttls()
            conn.login(my_email, my_pass)
            conn.sendmail(from_addr=my_email, to_addrs=my_email, msg="Subject:Look up\n\n The ISS is above you now")