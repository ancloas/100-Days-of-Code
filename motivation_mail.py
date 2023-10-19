import smtplib
from dotenv import load_dotenv
import os
import datetime as dt

load_dotenv()
Gmail_APP_Password=os.getenv('Gmail_APP_Password')
my_email=os.getenv('my_email')
recipient_email=os.getenv('recipient_email')

def send_mail(subject, msg_content, sender=my_email, password= Gmail_APP_Password, receiver=recipient_email):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        #start tls
        connection.starttls()
        connection.login(user=sender, password=password)
        connection.sendmail(from_addr=sender, 
                            to_addrs=receiver, 
                            msg=f"Subject: {subject}\n\n{msg_content}"
                            )


def get_new_quote():
    import re
    import random as rd
    quote={}
    with open('./quotes.txt', 'r') as file:
        quote_pattern= r'"\w*"'
        data = file.readlines()
        string= rd.choice(data)
        # string='"I was thinking one day and I realized that if I just had somebody behind me all the way to motivate me I could make a big difference. Nobody came along like that so I just became that person for myself." - Unknown asdf'
        quote_pattern = r'"(.*?)"\s*-\s* (\w+(\s\w+)?)'
        # Use re.search() to find the match and extract the quote and person
        match = re.search(quote_pattern, string)
        if match:
            return(match.group(1), match.group(2))  # Extract the quote
    return ('Good Morning!', 'Anugrah Gupta')



def send_weekly_mail(weekday):
    now=dt.datetime.now()
    print(now.weekday())
    if now.weekday()== weekday and now.hour>=8:
        quote=get_new_quote()
        send_mail(subject='Weekly Motivation', msg_content=f'''Good Morning\n Today's Quote: "{quote[0]}" ~ {quote[1]}''')
        print('mail sent!')
        


send_weekly_mail(3)