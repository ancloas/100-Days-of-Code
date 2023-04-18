from turtle import Turtle, Screen
from random import randint, choice

def rand_color():
    r=randint(0, 255)
    g=randint(0, 255)
    b=randint(0, 255) 
    return (r, g, b)
    

leo= Turtle()
leo.shape('turtle')
mike=Turtle()
mike.shape('turtle')
mike.color('green')

screen= Screen()
screen.colormode(255)


leo.speed('fast')
mike.speed('fastest')
directions=[0, 90, 180, 270]
leo.pensize(10)
mike.pensize(10)
for i in range(300):
    #random color   
    leo.color(rand_color())
    mike.color(rand_color())
    #random  choice
    leo.forward(30)
    leo.setheading(choice(directions))
    mike.forward(30)
    mike.right(randint(0, 30))

        








screen.exitonclick()