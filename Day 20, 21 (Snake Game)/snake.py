from turtle import Turtle
import copy


UP=90
DOWN=270
RIGHT=0
LEFT=180


class Snake_Segment(Turtle):
    def __init__(self, position: tuple, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True, direction: float=0, color: str = 'white') -> None:
        super().__init__('square', undobuffersize, visible)
        self.setheading(direction)
        self.setposition(position)
        self.color(color)
        self.penup()
        self.shapesize(0.5, 0.5)
        self.width=self.shapesize()[0]*20
        self.height=self.shapesize()[1]*20
    
    

    def set_snake_pos_behind(self, snake_part):
        self.setposition(snake_part.position())
        self.setheading(snake_part.heading())
        if snake_part.heading()==0:
            self.setx(self.xcor()- 20*snake_part.shapesize()[0])
        if snake_part.heading()==90:
            self.sety(self.ycor()+ 20*snake_part.shapesize()[1])
        if snake_part.heading()==180:
            self.setx(self.xcor() + 20*snake_part.shapesize()[0])
        if snake_part.heading()==270:
            self.setx(self.ycor()-20*snake_part.shapesize()[1])
    
    def follow(self, snake_part):
        self.goto(snake_part.position())
        self.setheading(snake_part.heading())


    def get_right(self):
        return self.xcor() + self.width/2 # type: ignore


    def get_left(self):
        return self.xcor() - self.width/2 # type: ignore


    def get_top(self):
        return self.ycor() + self.width/2 # type: ignore


    def get_bottom(self):
        return self.ycor() - self.width/2 # type: ignore
    
    def collision_with_segment(self, segment):
        if self.get_right() > segment.get_left() and self.get_left() < segment.get_right():             
            if self.get_top() > segment.get_bottom() and self.get_bottom() < segment.get_top():        
                return True
        


class Snake:
    def __init__(self, direction, color) -> None:
        STARTING_POS=(0,0)        
        self.body=[]
        self.MOVE_DISTANCE=20 ## Move Distance
        self.points=0
        self.color=color
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
        self.head.forward(self.head.width)
    
    def grow_tail(self):
        tail=self.body[-1]
        new_tail=Snake_Segment(tail.position(), color=self.color, direction=tail.heading())
        self.body.append(new_tail)
        

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


    def eats_food(self):
        self.points+=1
        self.grow_tail()

    
    def is_hitself(self):
        for i in range(1,len(self.body)):
            if self.head.collision_with_segment(self.body[i]):
                return True

    def is_hitwall(self, Wall_Width, Wall_height):
        if self.head.get_right()>=Wall_Width/2:
            return True
        if self.head.get_left()<=-Wall_Width/2:
            return True
        if self.head.get_top()>=Wall_height/2:
            return True
        if self.head.get_bottom()<=-Wall_height/2:
            return True




