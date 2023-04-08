from art import logo, vs
from game_data import data
import random
import os

def compare_accounts(a, b, choice):
    if choice.lower()=='a':
        if a['follower_count']>=b['follower_count']:
            return True
        else:
            return False
        
    if choice.lower()=='b':
        if a['follower_count']>=b['follower_count']:
            return False
        else:
            return True
    return False


def represent_account(a):
    return f"{a['name']}, {a['description']}, from {a['country']}"




def game_higher_lower(a=None, score=0):
    if a==None:
        a=random.choice(data)   
    
    b= random.choice(data)   
    while b==a:
        b= random.choice(data, )   

    
    print(logo)

    if score>0:
        print(f"You're right! your current score is {score}")

    print('Compare A: '+ represent_account(a))
    print(vs)
    print('Against B: '+ represent_account(b))

    choosen_account=input('Which account has mose more followers A or B? ')
    is_correct=compare_accounts(a,b,choosen_account)
    
    os.system('cls')
    if is_correct ==True:
        score+=1
        return game_higher_lower(b,score)
    

    print(logo)
    print(f"Sorry that's wrong, final score: {score},{a['name']}'s followers are {a['follower_count']}m, while {b['name']}'s followers are  {b['follower_count']}m")
    return


game_higher_lower()