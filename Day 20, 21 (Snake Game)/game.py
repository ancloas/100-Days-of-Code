from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from random import randint
from scoreboard import Scoreboard

SCREEN_WIDTH=600
SCREEN_HEIGHT=600


screen= Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor('black')
screen.title("My Snake Game")
screen.tracer(0) # turn off animation

## Create Snake
snake=Snake(180,'green')
food= Food((randint(-SCREEN_WIDTH//2 , SCREEN_WIDTH//2), randint(-SCREEN_HEIGHT//2, SCREEN_HEIGHT//2)))
score_writer=Scoreboard()


game_is_on=True



while game_is_on==True:
    screen.update()
    score_writer.update_scoreboard()
    time.sleep(.1)    
    if food.is_eaten(snake):
        snake.grow_tail()
        score_writer.increase_score()
        food.setposition(randint(-SCREEN_WIDTH//2 +10 , SCREEN_WIDTH//2-10), randint(-SCREEN_HEIGHT//2 +10, SCREEN_HEIGHT//2 -10))
        print(food.position())

    if snake.is_hitwall(Wall_Width=SCREEN_WIDTH,Wall_height=SCREEN_HEIGHT) or snake.is_hitself():
        score_writer.reset()  
        snake.reset()
    snake.start_moveing()

    screen.onkey(fun=snake.up, key='Up')
    screen.onkey(fun=snake.down, key='Down')
    screen.onkey(fun=snake.left, key='Left')
    screen.onkey(fun=snake.right, key='Right')
    screen.listen()
 

writer = Turtle(visible=False)
writer.color('Pink')
writer.write('Game Over')
screen.update()

    







screen.exitonclick()