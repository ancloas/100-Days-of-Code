from turtle import Turtle, Screen
from random import randint, choice
import colorgram


def rand_color():
    r=randint(0, 255)
    g=randint(0, 255)
    b=randint(0, 255) 
    return (r, g, b)
    
colors = colorgram.extract('Day_18\image.jpg', 10)
colors_list=[]

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    
    colors_list.append((r, g, b))

print(colors_list)

for color in colors_list:
    if color[0]+color[1]+color[2]>660:
        colors_list.remove(color)

screen= Screen()
screen.colormode(255)



leo= Turtle()
leo.shape('circle')
leo.speed('fastest')

leo.hideturtle()
leo.penup()
leo.setpos(-230, -230)
x_pos, y_pos= leo.position()


for i in range(10):
    for j in range(10):
        leo.pendown()        
        leo.dot(20, choice(colors_list))
        leo.penup()
        leo.forward(50)
    leo.setx(x_pos)
    leo.sety(leo.position()[1]+50)





screen.exitonclick()