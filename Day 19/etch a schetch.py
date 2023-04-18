from turtle import Turtle, Screen

leo=Turtle()
screen=Screen()
leo.shape('turtle')


def move_forward():
    leo.forward(10)


def move_backward():
    leo.backward(10)


def tilt_clockwise():
    leo.right(10)


def tilt_anti_clockwise():
    leo.left(10)    

screen.onkey(key="w",fun= move_forward)
screen.onkey(key="s",fun= move_backward)
screen.onkey(key="a",fun= tilt_anti_clockwise)
screen.onkey(key="d",fun= tilt_clockwise)
screen.onkey(key="c",fun= leo.reset)


screen.listen()


screen.exitonclick()