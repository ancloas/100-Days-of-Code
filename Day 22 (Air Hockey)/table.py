from rectangle import Rectangle
from turtle import Turtle

class Table(Rectangle):
    def __init__(self, undobuffersize: int = 1000, visible: bool = True, position: tuple = ..., length: int = 20, height: int = 20, color: str ='white') -> None:
        super().__init__(undobuffersize, visible, (0, 0), length, height) # type: ignore
        self.pencolor('black')
        self.fillcolor(color)
        self.right_goal_post= Rectangle(length=3, height=self.height//5, position=(self.get_right(), 0))
        self.left_goal_post= Rectangle(length=3, height=self.height//5, position=(self.get_left(),0))
        self.centre_line= Rectangle(length=1, height=self.height, position=(0,0))
        




