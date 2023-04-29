from rectangle import Rectangle
from random import randint
from turtle import Vec2D

class Ball(Rectangle):
    def __init__(self, undobuffersize: int = 1000, visible: bool = True, position: tuple = (0, 0), length: int = 20, height: int = 20) -> None:
        super().__init__(undobuffersize, visible, position, length, height)
        self.serv(direction='right')
    
    def serv(self, direction):
        if direction.lower()=='right':
            self.velocity=Vec2D(randint(1,2), randint(-2,2))
        if direction.lower()=='left':
            self.velocity=Vec2D(randint(-2,-1), randint(-2,2))


    def after_hit_wall(self, wall):
        if_hit= self.hit_wall(wall)
        if if_hit ==1:
            self.reflect_Y_velocity()

        if if_hit ==-1:
            self.reflect_X_velocity()