import datetime as dt
from smtplib import SMTP
import pandas
import random

# Email variables
my_email = "pythonmaster56@gmail.com"
my_pass = "jqgu ardd vyfe nkpv"

data = pandas.read_csv("birthdays.csv")
birthday_dict = {(row.month, row.date): row.to_dict() for _,row in data.iterrows()}

now = dt.datetime.now()
today_month, today_date = now.month, now.day

if (today_month, today_date) in birthday_dict:
    person_info = birthday_dict[(today_month, today_date)]
    letter_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    
    with open(letter_path) as file:
        letters = file.read()
    
    final_letter= letters.replace('[NAME]', person_info['name'])
    print(final_letter)
        
    with SMTP("smtp.gmail.com") as conn:
        conn.starttls()
        conn.login(my_email, my_pass)
        conn.sendmail(from_addr=my_email, to_addrs=person_info['email'], 
        msg=f"Subject: Happy Birthday\n\n{final_letter}")