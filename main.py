import html
from dotenv import load_dotenv
import os

# from ui import QuizInterface
import requests
import pandas as pd
from datetime import datetime, time
from message import send_message

rain_alert_icon=['10', '11', '12', '13', '14', '15', '20', '21', '22', '23', '24', '25']
load_dotenv()
api_key = os.environ['api_key']


def get_hourly_forecast(city_name):

    parameters={'place_id': f'{city_name}',
               'sections':'hourly',
               'language': 'en',
               'units': 'metric',
               'key': api_key
               
               }
    response= requests.get(url='https://www.meteosource.com/api/v1/free/point?', params=parameters)
    response.raise_for_status()
    return response.json()['hourly']['data']

def rain_alert(city_name):
    
    # Get today's date
    today_date = datetime.today().date()

    # Create a datetime object for 8 AM
    going_off_time = datetime.combine(today_date, time(8, 0))
    get_back_time = datetime.combine(today_date, time(19, 0))

    data=get_hourly_forecast(city_name)
    df= pd.DataFrame(data)
    df['date']=pd.to_datetime(df['date'])
    df = df[(df['date'] >= going_off_time) & (df['date'] <= get_back_time)]
    result = df['icon'].isin(rain_alert_icon).any()
    if result:
        send_message(mssg_body='Helllo! I thing today it will rain, so get your umberalla')

# print(get_current_weather_info('indore', 'IN'))
print(rain_alert('delhi'))