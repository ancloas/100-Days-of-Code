from turtle import Turtle

UP=90
DOWN=270
RIGHT=0
LEFT=180


class Snake_Segment(Turtle):
    def __init__(self,  position: tuple, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True, direction: float=0, color: str = 'white') -> None:
        super().__init__('square', undobuffersize, visible)
        self.setheading(direction)
        self.setposition(position)
        self.color(color)
        self.penup()
 

    def set_snake_pos_behind(self, snake_part):
        self.setposition(snake_part.position())
        self.setheading(snake_part.heading())
        if snake_part.heading()==0:
            self.setx(self.xcor()- 20*snake_part.shapesize()[0] -2)
        if snake_part.heading()==90:
            self.sety(self.ycor()+ 20*snake_part.shapesize()[1] +2)
        if snake_part.heading()==180:
            self.setx(self.xcor() + 20*snake_part.shapesize()[0] +2)
        if snake_part.heading()==270:
            self.setx(self.ycor()-20*snake_part.shapesize()[1] + 2)
    
    def follow(self, snake_part):
        self.goto(snake_part.position())
        self.setheading(snake_part.heading())
        

class Snake:
    def __init__(self, direction, color) -> None:
        STARTING_POS=(0,0)        
        self.body=[]
        self.MOVE_DISTANCE=20 ## Move Distance
        for i in range(3):
            body_part=Snake_Segment(position= STARTING_POS, direction = direction, color = color)
            if i==0:
                self.head=body_part
            else:
                body_part.set_snake_pos_behind(self.body[i-1])
            self.body.append(body_part)
       
        
    def start_moveing(self):

        for i in range(len(self.body)-1, 0, -1):
            self.body[i].follow(self.body[i-1])
        self.head.forward(self.MOVE_DISTANCE)
    


    def up(self):
        if  self.head.heading()==DOWN:
            return
        self.head.setheading(UP)


    def left(self):
        if  self.head.heading()==RIGHT:
            return
        self.head.setheading(LEFT)

    def right(self):
        if  self.head.heading()==LEFT:
            return
        self.head.setheading(RIGHT)

    def down(self):
        if  self.head.heading()==UP:
            return
        self.head.setheading(DOWN)




