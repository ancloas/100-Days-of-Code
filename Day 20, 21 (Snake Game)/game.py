from turtle import Screen, Turtle
import time
from snake import Snake


screen= Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("My Snake Game")
screen.tracer(0) # turn off animation

## Create Snake
snake=Snake(180,'green')

game_is_on=True



while game_is_on==True:
    screen.update()
    time.sleep(.1)    
    snake.start_moveing()
    screen.onkey(fun=snake.up, key='Up')
    screen.onkey(fun=snake.down, key='Down')
    screen.onkey(fun=snake.left, key='Left')
    screen.onkey(fun=snake.right, key='Right')
    screen.listen()
 

    








screen.exitonclick()