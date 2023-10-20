from tkinter import *
import requests
from datetime import datetime
import smtplib
from dotenv import load_dotenv
import os
import time


MY_LAT= 26.217431342099385
MY_LONG= 78.16147699598031

load_dotenv()
Gmail_APP_Password=os.getenv('Gmail_APP_Password')
my_email=os.getenv('my_email')
recipient_email=os.getenv('recipient_email')


def is_night_time():
    time_now=datetime.now()
    parameters={'lat': MY_LAT,
                'lang':MY_LONG,
                'formatted': 0
                }


    response=requests.get(url='https://api.sunrise-sunset.org/json', params=parameters)
    response.raise_for_status()
    data=response.json()
    sunrise_hour= data['results']['sunrise'].split('T')[1].split(':')[0]
    sunset_hour= data['results']['sunset'].split('T')[1].split(':')[0]
    if time_now.hour<int(sunrise_hour) or time_now.hour>int(sunset_hour):
        return 1    
    return 0

def get_iss_pos():
    response=requests.get(url='http://api.open-notify.org/iss-now.json')
    data= response.json()
    return data['iss_position']

def send_mail(subject, msg_content, sender=my_email, password= Gmail_APP_Password, receiver=recipient_email):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        #start tls
        connection.starttls()
        connection.login(user=sender, password=password)
        connection.sendmail(from_addr=sender, 
                            to_addrs=receiver, 
                            msg=f"Subject: {subject}\n\n{msg_content}"
                            )
    


def iss_position_overhead(iss_lat: float , iss_long: float, my_lat: float, my_long:float):
    if iss_lat>my_lat+5:
        return False
    
    if iss_lat<my_lat-5:
        return False 
    
    if iss_long>my_long+5:
        return False 
    
    if iss_long<my_long-5:
        return False 
    
    return True



def send_alert():
    if not is_night_time():
        return 

    iss_pos=get_iss_pos()
    iss_lat=float(iss_pos['latitude'])
    iss_long=float(iss_pos['longitude'])

    if not iss_position_overhead(my_lat=MY_LAT, my_long=MY_LONG, iss_lat=iss_lat, iss_long=iss_long):
        return
    send_mail('ISS overhead!', 'Go to the roof and look up the sky', sender=my_email, password= Gmail_APP_Password, receiver=recipient_email)
    send_alert()

print(send_alert())
