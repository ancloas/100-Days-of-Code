
from turtle import Turtle
from snake import Snake

class Food(Turtle):
    def __init__(self,  position: tuple, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True, direction: float=0, color: str = 'white') -> None:
        super().__init__('square', undobuffersize, visible)
        self.setheading(direction)
        self.setposition(position)
        self.color(color)
        self.shape('circle')
        self.shapesize(0.5,0.5)
        self.penup()
        self.width=self.shapesize()[0]*20
        self.height=self.shapesize()[1]*20
        
    
    def is_eaten(self, snake: Snake):
        if self.get_right() > snake.head.get_left() and self.get_left() < snake.head.get_right():             
            if self.get_top() > snake.head.get_bottom() and self.get_bottom() < snake.head.get_top():        
                return True

    def get_right(self):
        return self.xcor() + self.width/2 

    def get_left(self):
        return self.xcor() - self.width/2 

    def get_top(self):
        return self.ycor() + self.width/2 

    def get_bottom(self):
        return self.ycor() - self.width/2 

