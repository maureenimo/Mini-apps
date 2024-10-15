import requests
from datetime import datetime
import os

# Date & Time
today_date = datetime.now().strftime("%x")
today_hour = datetime.now().strftime("%X")

# Nutritionix

NUTRI_APP_ID = os.environ["ENV_NIX_APP_ID"]
NUTRI_APP_KEY =  os.environ["ENV_NIX_API_KEY"]
NUTRI_ENDPOINTS = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercises = input("Which exercise did you to: ")

headers = {
    "x-app-id": NUTRI_APP_ID,
    "x-app-key" : NUTRI_APP_KEY
}
parameters = {
    "query": exercises,
    "gender": "female",
    "weight_kg": 67,
    "height_cm": 167.00,
    "age":27
    
}

res = requests.post(NUTRI_ENDPOINTS, headers=headers, json= parameters)
result = res.json()
print(f"Nutritionix : {result}")

# Sheety
SHEETY_ENDPOINT = os.environ["ENV_SHEETY_ENDPOINT"]

for exercise in result['exercises']:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": today_hour,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        
        }
    }
    
res = requests.post(SHEETY_ENDPOINT , json=sheet_inputs)
print(res.text)
res = requests.get(SHEETY_ENDPOINT)
print(res.text)