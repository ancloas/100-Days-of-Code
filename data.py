import requests

def get_new_question(amount=10, category=11, difficulty='easy', question_type= 'boolean' ):
    parameters={
        'amount': amount,
        'category': category,
        'difficulty': difficulty,
        'encoding': 'url3986',
        'type': question_type
    }
    response= requests.get(url=f'https://opentdb.com/api.php?', params=parameters)
    response.raise_for_status()
    # quiz=[]
    # for data in response.json()['results']:
    #     question={}
    #     question['question']=data['question']
    #     question['answer']=data['correct_answer']
    #     question['incorrect_answers']=data['incorrect_answers']        
    #     quiz.append(question)
    return response.json()['results']

