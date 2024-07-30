import datetime as dt
from smtplib import SMTP
import random

# Email variables
my_email = "pythonmaster56@gmail.com"
my_pass = "jqgu ardd vyfe nkpv"

with open("quotes.txt") as data:
    all_quotes = data.readlines()
    
quote_of_day = random.choice(all_quotes)

now = dt.datetime.now()
days_of_week = now.weekday()

if days_of_week == 3:
    with SMTP("smtp.gmail.com", port= 587) as my_conn:
        my_conn.starttls()
        my_conn.login(my_email, my_pass)
        my_conn.sendmail(from_addr=my_email, to_addrs=my_email, msg=f"Subject:Quote of the day\n\n{quote_of_day}")
        
