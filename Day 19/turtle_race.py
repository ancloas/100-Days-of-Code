from turtle import Turtle, Screen
from random import choice,randint

colors=['red', 'green', 'yellow', 'purple', 'blue', 'orange', 'violet', 'indigo']

screen= Screen()
screen.setup(width=500, height=400)

def create_turtle(color, x_pos, y_pos):
    turtle = Turtle(shape='turtle', visible=False)
    turtle.shape('turtle')
    turtle.penup()
    turtle.color(color)
    turtle.goto(x_pos, y_pos)
    turtle.showturtle()
    return turtle



betted_turtle= str(screen.textinput(title='Make a bet', prompt='Please choose the color of winning turtle'))

turtles=[]
y_pos=100
x_pos=-240
for color in colors:
    turtles.append(create_turtle(color, x_pos, y_pos))
    y_pos-=20

is_race_on=True
winner=''
while is_race_on:
    for i in range(len(turtles)):
        turtles[i].forward(randint(0,10))
        if turtles[i].xcor()>=230:
            is_race_on=False
            winner=colors[i]

if winner.lower() == betted_turtle.lower():
    print('You win')
else: 
    print("You lose")

print(f"winner is {winner} turtle")

screen.exitonclick()