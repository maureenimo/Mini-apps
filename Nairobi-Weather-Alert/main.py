import requests
from twilio.rest import Client

api_key = "b6a9d2b1ffe2c427f9d1db952cf74079"
account_sid = "YOUR SID"
auth_token = "YOUR AUTH_TOKEN"


parameters = {
    "lat": -0.023559,
    "lon": 37.906193, 
    "cnt": 3,
    "appid": api_key
}

res = requests.get("https://api.openweathermap.org/data/2.5/forecast", params= parameters)
res.raise_for_status()
weather_data = res.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = int(hour_data["weather"][0]["id"])
    if condition_code <= 600:
       will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    
    message = client.messages.create(
        body="Today will be sunny. Let's go swimming.",
        from_="+15017122661",
        to="+15558675310",
    )
    
    print(message.body)