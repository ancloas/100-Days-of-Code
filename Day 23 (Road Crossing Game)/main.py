import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from random import randint
from turtle import Turtle

WIDTH=600
HEIGHT=600

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.tracer(0)
player= Player(position=( 0, -HEIGHT//2))
carmanager= CarManager(screen_height=HEIGHT, screen_width=WIDTH)
score_board= Scoreboard(position=(-WIDTH//2 +60, HEIGHT//2-60))


finish_line= Turtle(visible=False)
finish_line.penup()
finish_line.setpos(- WIDTH//2, HEIGHT//2-20)
finish_line.pendown()
finish_line.goto(WIDTH//2, HEIGHT//2-20)




game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    score_board.draw_level(carmanager.level)
    screen.onkeypress(key='Up', fun=player.move)



    if not carmanager.if_max_cars():
            carmanager.add_car()
    carmanager.move()
    if carmanager.is_Accident(player):
        game_is_on=False
        player.setpos(-WIDTH//2, 0)
    if player.is_Reached_Finish(finish_line=WIDTH//2-20):
        screen.clear()
        player = Player(position=( 0, -HEIGHT//2))
        carmanager.level_up()

    screen.listen()
        