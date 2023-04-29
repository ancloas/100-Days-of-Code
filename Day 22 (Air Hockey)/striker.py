from rectangle import Rectangle


class Striker(Rectangle):
    def __init__(self, undobuffersize: int = 1000, visible: bool = True, position: tuple = (0,0), length: int = 30, height: int = 100, color: str = 'Blue') -> None:
        super().__init__(undobuffersize, visible, position, length, height)
        self.color(color)
        self.score=0
    
    def hit_ball(self, ball: Rectangle):
        if (not self.detect_collision(ball)):
            return 
        
        ball.reflect_X_velocity()
        ball.increase_X_velocity(self.velocity[0]*2)  # type: ignore
        
        if ball.position()[0]-self.position()[0]>=0:
            ball.setpos(self.get_right()+ball.width+5, ball.position()[1])
        if ball.position()[0]-self.position()[0]<0:
            ball.setpos(ball.get_left()-ball.width-5, ball.position()[1])
            

    def move_up(self):
        self.increase_Y_velocity(1)


    def move_down(self):
        self.decrease_Y_velocity(1)


    def move_right(self):
        self.increase_X_velocity(1)


    def move_left(self):
        self.decrease_X_velocity(1)

        
    def after_hit_wall(self, wall):
        if_hit= self.hit_wall(wall)
        if if_hit ==1:
            self.reset_velocity_Y()

        if if_hit ==-1:
            self.reset_velocity_X()

    def increase_score(self):
        self.score+=1