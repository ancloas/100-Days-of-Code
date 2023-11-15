import requests
from datetime import date

def create_new_user(token, username, age):
    pixela_endpoint= "https://pixe.la/v1/users"

    if age<18:
        return "You are minor can't create account"
    
    user_params= {
        'token':token,
        'username': username,
        "agreeTermsOfService":"yes",
        "notMinor":"yes"
    }
    

    response = requests.post(url= pixela_endpoint, json=user_params)
    response.raise_for_status() 
    print(response.text)                  



def create_a_graph(token, username, graph_id, graph_name, graph_unit, type_of_quantity='int', color='momiji', ):
    end_point= f'https://pixe.la/v1/users/{username}/graphs'

    headers={
        'X-USER-TOKEN': token
    }

    user_params={
        "id": graph_id,
        "name":graph_name, 
        "unit": graph_unit,
        "type": type_of_quantity,
        "color": color,
     }
    

    response = requests.post(url= end_point, json=user_params, headers=headers)
    response.raise_for_status() 
    print(response.text)       


def add_a_pixel(token, username, graph_id, date, quantity):
    end_point= f'https://pixe.la//v1/users/{username}/graphs/{graph_id}'

    headers={
        'X-USER-TOKEN': token
    }

    user_params={
        "date": date,
        "quantity":quantity, 
     }
    

    response = requests.post(url= end_point, json=user_params, headers=headers)
    response.raise_for_status() 
    print(response.text)       


def add_a_pixel_today(token, username, graph_id, quantity):
    today = date.today()
    formatted_date = today.strftime("%Y%m%d")
    return add_a_pixel(token, username, graph_id, formatted_date, quantity)
    

def update_a_pixel(token, username, graph_id, date,  quantity):
    end_point= f'https://pixe.la//v1/users/{username}/graphs/{graph_id}/{date}'

    headers={
        'X-USER-TOKEN': token
    }

    user_params={
        "quantity":quantity
     }
    

    response = requests.put(url= end_point, json=user_params, headers=headers)
    response.raise_for_status() 
    print(response.text)       



def delete_a_pixel(token, username, graph_id, date):
    end_point= f'https://pixe.la//v1/users/{username}/graphs/{graph_id}/{date}'

    headers={
        'X-USER-TOKEN': token
    }


    response = requests.delete(url= end_point, headers=headers)
    response.raise_for_status() 
    print(response.text)       



#create_new_user('secret101', 'ancloas123', 19)
# create_a_graph('secret101', 'ancloas123', 'habitread12','reading_habit', 'page', 'int', 'shibafu')
# add_a_pixel_today('secret101', 'ancloas123', 'habitread12' ,'5')
# update_a_pixel('secret101', 'ancloas123', 'habitread12','20231115' ,'2')
delete_a_pixel('secret101', 'ancloas123', 'habitread12','20231115')