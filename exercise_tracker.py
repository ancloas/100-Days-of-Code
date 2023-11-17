import requests
from dotenv import load_dotenv
import os
from datetime import datetime
import pandas as pd

load_dotenv()

end_point_nutrients=  'https://trackapi.nutritionix.com/v2/natural/exercise'


def get_exercise_stats_from_sentence(sentence: str, gender: str='male', weight_kg:float=72.5, height_cm:float = 167.64, age:int= 23):
    end_point_nutrients=  'https://trackapi.nutritionix.com/v2/natural/exercise'

    
    header={
       'x-app-id' : os.getenv('NUTRITIONIX_APP_ID'),
       'x-app-key' : os.getenv('NUTRITIONIX_API_KEY'),
       'x-remote-user-id': '0'
    }
    json_data= {
    "query":sentence,
    
    }   
    response= requests.post(url=end_point_nutrients, json=json_data, headers=header)
    response.raise_for_status()
    exercises= response.json()['exercises']
    # exercise_stats={
    #     'Time': [],
    #     'Date': [],
    #     'Exercise':  [],
    #     'Duration':  [],
    #     'Calories':  []
    # }
    exercise_list=[]
    date= datetime.now()
    curr_date= date.strftime('%Y-%m-%d')
    curr_time= date.strftime('%H:%M:%S')
    
    for exercise in exercises:
        dict={}
        dict['calories']= exercise['nf_calories']
        dict['duration']=exercise['duration_min']
        dict['exercise']=exercise['name']
        dict['date']=curr_date     
        dict['time']=curr_time
        exercise_list.append(dict)

    return exercise_list


def get_sheet_data(Endpoint_var:str):
    url= os.getenv(Endpoint_var)
    secret= os.getenv('BEARER_SECRET')
    header= {'Authorization': f'Bearer {secret}'}
    response= requests.get(url, headers=header) 
    response.raise_for_status()
    return response.text


def post_sheet_data(Endpoint_var:str, datapoint:dict):
    url= os.getenv(Endpoint_var)
    secret= os.getenv('BEARER_SECRET')
    header= {'Authorization': f'Bearer {secret}'}
    data= {'workout': datapoint}
    response= requests.post(url, json=data, headers=header) 
    response.raise_for_status()
    return response.text

def post_multiple_sheets(Endpoint_var:str, datapoints:list):
    for data in datapoints:
        post_sheet_data(Endpoint_var, data)
    return 'Success'
# print(get_exercise_stats_from_sentence('I travelled 8km to my college by bicycle but had to walk home as bicylce broke', gender='male', weight_kg=71, height_cm=172, age=25))   
datapoints= get_exercise_stats_from_sentence('I travelled 8km to my college by bicycle but had to walk home as bicylce broke', gender='male', weight_kg=71, height_cm=172, age=25)
print(post_multiple_sheets('SHEETY_ENDPOINT_WORKOUT', datapoints))