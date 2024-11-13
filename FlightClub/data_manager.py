import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
from pprint import pprint

# Load environment variables
load_dotenv()

# Sheety API endpoint
SHEETY_ENDPOINT = "https://api.sheety.co/"

class DataManager:
    def __init__(self):
        self._user = os.environ.get("SHEETY_USERNAME")
        self._password = os.environ.get("SHEETY_PASSWORD")
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(SHEETY_ENDPOINT, auth=self._authorization)
        results = response.json()
        pprint(results) 
        
        self.destination_data = results['prices']
        
        return self.destination_data

    def update_data(self):
        for city in self.destination_data: 
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            
            # Send PUT request with authentication
            response = requests.put(
                url=f"{SHEETY_ENDPOINT}/{city['id']}",
                json=new_data,
                auth=self._authorization
            )
            
            pprint(response.text)
