import smtplib
from dotenv import load_dotenv
import os
import datetime as dt
import pandas as pd
import random as rd


lettter_dir = './letters'

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


def get_the_letter(recepitent, sender):
    letters = os.listdir(lettter_dir)
    random_letter = rd.choice(letters)
    with open(os.path.join(lettter_dir, random_letter), 'r', encoding='utf-8') as template_file:
        output_text = template_file.read()
        output_text = output_text.replace(f'[Sender]', sender)
        output_text = output_text.replace(f'[Recipient]', recepitent)
    return output_text





def give_today_birthdays(day, month):
    birthdays= pd.read_csv('./data/birthdays.csv')
    birthdays=birthdays[(birthdays['Day']==day) & (birthdays['Month']==month)]
    return birthdays[['Name','Email']]


def send_birthday_mail():
    now=dt.datetime.now()
    friends_with_birthday=give_today_birthdays(now.day, now.month)
    for index, row in friends_with_birthday.iterrows():
        letter=get_the_letter(recepitent=row['Name'], sender='Anugrah')
        send_mail(receiver=row['Email'],subject='Happy Birthday!', msg_content=f'''{letter}''')
        print('mail sent!')


send_birthday_mail()