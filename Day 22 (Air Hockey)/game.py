from turtle import Screen
from table import Table
from ball import Ball
from striker import Striker
from scoreboard import ScoreCard
from time import sleep



HEIGHT=600
WIDTH=800

screen= Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor('green')
screen.title("My Air Hockey Game")
screen.tracer(0) # turn off animation



table = Table(color='pink', height=HEIGHT-100, length=WIDTH-50)
ball = Ball()
player1= Striker(color='Green', position=(table.get_left()+50, 0))
player1.setheading(0)
player2= Striker(color= 'Yellow', position=(table.get_right()-50, 0))
player2.setheading(180)
left_scorecard= ScoreCard(position=(-50,HEIGHT/2-50))
right_scorecard= ScoreCard(position=(50,HEIGHT/2-50))



game_is_on=True
score=False
direction='right'


while(game_is_on):

    if score:
        ball.setpos(0,0)
        if direction=='right':
            direction='left'
        else: direction='right'
        ball.serv(direction)
        player1.setpos((table.get_left()+50, 0))
        player2.setpos((table.get_right()-50, 0))
        left_scorecard.print_score(player1.score)
        right_scorecard.print_score(player2.score)
        score=False
        if player1.score>5 or player2.score >5:
            game_is_on=False

    screen.update()

    player1.hit_ball(ball)
    player1.after_hit_wall(table)
    player2.hit_ball(ball)
    player2.after_hit_wall(table)
    
    if ball.detect_collision(table.right_goal_post):
        player1.increase_score()
        score=True

    if ball.detect_collision(table.left_goal_post):
        player2.increase_score()
        score=True


    ball.after_hit_wall(table)


    screen.onkeypress(fun=player1.move_up, key='w')
    screen.onkeypress(fun=player1.move_left, key='a')
    screen.onkeypress(fun=player1.move_right, key='d')
    screen.onkeypress(fun=player1.move_down, key='s')
    
    
    screen.onkeypress(fun=player2.move_up, key='Up')
    screen.onkeypress(fun=player2.move_left, key='Left')
    screen.onkeypress(fun=player2.move_right, key='Right')
    screen.onkeypress(fun=player2.move_down, key='Down')



    player1.move()
    player2.move()
    ball.move()


    screen.onkeyrelease(fun=player1.reset_velocity_Y, key='w')
    screen.onkeyrelease(fun=player1.reset_velocity_X, key='a')
    screen.onkeyrelease(fun=player1.reset_velocity_X, key='d')
    screen.onkeyrelease(fun=player1.reset_velocity_Y, key='s') 

    screen.onkeyrelease(fun=player2.reset_velocity_Y, key='Up')
    screen.onkeyrelease(fun=player2.reset_velocity_X, key='Left')
    screen.onkeyrelease(fun=player2.reset_velocity_X, key='Right')
    screen.onkeyrelease(fun=player2.reset_velocity_Y, key='Down')  
    screen.listen()


left_scorecard.penup()
left_scorecard.setpos(0,0)
left_scorecard.pendown()
left_scorecard.write('Game Over')
        

    
  
    




screen.exitonclick()

