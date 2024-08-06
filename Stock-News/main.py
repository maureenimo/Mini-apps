import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
AVALANCHE_URL = "https://www.alphavantage.co/query"

NEWS_API = "api_key"
AVALANCHE_API_KEY = "api_key"
TWILIO_SID = "sid_num"
TWILIO_AUTH_TOKEN = "auth_token"
AVALANCHE_PARAMETERS = f"function=TIME_SERIES_DAILY&symbol={STOCK_NAME}&apikey={AVALANCHE_API_KEY}"

response = requests.get(AVALANCHE_URL, AVALANCHE_PARAMETERS)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]

closing_price = [value for (key,value) in data.items()]
print(closing_price)
yesterday_closing = float(closing_price[0]["4. close"])
day_before_yesterday_closing = float(closing_price[1]["4. close"])
print(yesterday_closing, day_before_yesterday_closing)

difference = abs(yesterday_closing - day_before_yesterday_closing)
percentage_difference = (difference / yesterday_closing) * 100
print(difference, percentage_difference)

if percentage_difference < 5:
    # News API endpoint
    NEWS_API_URL = f"https://newsapi.org/v2/everything?q={COMPANY_NAME}&apiKey={NEWS_API}"
    news_response = requests.get(NEWS_API_URL)
    articles = news_response.json()["articles"][:3] 
    print(articles)
    
    # Twilio client setup
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    for article in articles:
        headline = article["title"]
        brief = article["description"]
        message_body = f"{STOCK_NAME}: 🔺{round(percentage_difference, 2)}%\nHeadline: {headline}\nBrief: {brief}"
        print(message_body)
        # Send SMS
        message = client.messages.create(
            body= message_body,
            from_= "sid no",
            to= "yourverifiedno"
        )
        print(f"Message sent: {message.sid}")
