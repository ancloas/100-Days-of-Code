from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from random import randint


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
score_writer=Turtle(visible=False)
score_writer.color('yellow')
score_writer.penup()
score_writer.setposition(0,280)
score_writer.penup()

game_is_on=True



while game_is_on==True:
    screen.update()
    score_writer.clear()
    score_writer.write(f'Score: {snake.points}')
    time.sleep(.1)    
    if food.is_eaten(snake):
        snake.eats_food()
        food.setposition(randint(-SCREEN_WIDTH//2 +10 , SCREEN_WIDTH//2-10), randint(-SCREEN_HEIGHT//2 +10, SCREEN_HEIGHT//2 -10))
        print(food.position())

    if snake.is_hitwall(Wall_Width=SCREEN_WIDTH,Wall_height=SCREEN_HEIGHT):
        game_is_on=False    

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