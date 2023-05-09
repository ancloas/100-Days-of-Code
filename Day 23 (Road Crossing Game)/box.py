from turtle import Turtle
from turtle import Vec2D
class Box(Turtle):
    def __init__(self, undobuffersize: int = 1000, visible: bool = True, position: tuple = (0, 0), width: int=20, height:int =20) -> None:
        super().__init__('square', undobuffersize, False)
        self.penup()
        self.hideturtle()
        self.setpos(position)
        self.shapesize(stretch_len=width/20, stretch_wid=height/20)
        self.height=height
        self.width=width
        self.velocity=Vec2D(0,0)
        self.showturtle()
    
    def get_right(self):
        return self.xcor() + self.width/2 # type: ignore


    def get_left(self):
        return self.xcor() - self.width/2 # type: ignore


    def get_top(self):
        return self.ycor() + self.height/2 # type: ignore


    def get_bottom(self):
        return self.ycor() - self.height/2 # type: ignore
            
        
    def detect_collision(self, rectangle):
        if self.get_right() > rectangle.get_left() and self.get_left() < rectangle.get_right():             
            if self.get_top() > rectangle.get_bottom() and self.get_bottom() < rectangle.get_top():        
                return True
            
    
    def move(self):
        if type(self.velocity) ==int:
            print(self.velocity)

        self.setposition(self.position().__add__(self.velocity)) # type: ignore


    def increase_X_velocity(self, increment):
        self.velocity=self.velocity.__add__(Vec2D(increment, 0)) # type: ignore


    def decrease_X_velocity(self, increment):
        self.increase_X_velocity(-1*increment)
    

    def increase_Y_velocity(self, increment):
        self.velocity=self.velocity.__add__(Vec2D(0,increment))  # type: ignore


    def decrease_Y_velocity(self, increment):
        self.increase_Y_velocity(-1*increment)


    def reflect_X_velocity(self):
        self.velocity=Vec2D(-1*self.velocity[0], self.velocity[1])
        


    
    def reflect_Y_velocity(self):
        self.velocity=Vec2D(self.velocity[0], -1*self.velocity[1])




    def reset_velocity_X(self):
        self.velocity=Vec2D(0, self.velocity[1])

    def reset_velocity_Y(self):
        self.velocity=Vec2D(self.velocity[0], 0)


    def hit_wall(self, wall):
        if self.get_left() <= wall.get_left():
            self.setposition(wall.get_left()+ (self.width)/2 + 5 , self.position()[1]) 
            return -1

        if self.get_right() >= wall.get_right():
            self.setposition(wall.get_right()- (self.width)/2  -5 , self.position()[1])                          
            return -1
        if self.get_top() >= wall.get_top():
            self.setposition(self.position()[0], wall.get_top()- (self.height)/2 -5 )              
            return 1

        if self.get_bottom() <= wall.get_bottom():       
            self.setposition(self.position()[0], wall.get_bottom()+ (self.height)/2 +5)              
            return 1
    
        return 0
