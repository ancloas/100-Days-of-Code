import turtle
import pandas as pd

df=pd.read_csv("data/50_states.csv")

def get_position_coordinates_from_state_name(state_name: str):
    return tuple(df[df.state.str.lower() == state_name.lower()][["x", "y"]].iloc[0])  
    

def check_statename_in_data(state_name: str):
    return sum(df.state.str.lower() == state_name.lower())

screen = turtle.Screen()
screen.title("U.s State Game")
image= "blank_states_img.gif"

screen.addshape(image)

turtle.shape(image)

writer= turtle.Turtle(visible=False)
writer.penup()

def get_mouse_click_coor(x, y):
    print(x, y)

turtle.onscreenclick(get_mouse_click_coor)
guess_count=0
correct_guesses=[]

while guess_count<70:
    answer_state=screen.textinput(title=f"Guess the State ({len(correct_guesses)}/{guess_count}) ", prompt="What's another state's name?")

    if answer_state.lower() == "exit":
        break

    if answer_state not in correct_guesses and check_statename_in_data(answer_state):
        position=get_position_coordinates_from_state_name(answer_state)
        writer.goto(position)
        writer.write(answer_state)
        correct_guesses.append(answer_state.title())
    guess_count+=1


data_to_learn= df[~df['state'].isin(correct_guesses)]['state']
data_to_learn.to_csv("data/to_learn_states.csv")

