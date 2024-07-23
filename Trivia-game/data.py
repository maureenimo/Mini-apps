import requests

data = requests.get("https://opentdb.com/api.php?amount=30&type=boolean")
data.raise_for_status()
question_data = data.json()["results"] 