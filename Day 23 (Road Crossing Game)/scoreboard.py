from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self, position: tuple,  shape: str = "classic", undobuffersize: int = 1000, visible: bool = False) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.setpos(position)
        self.penup()
        
    def draw_level(self, level: int):
        self.clear()
        self.pendown()
        self.write('Level ' + str(level), font=FONT)
        self.penup()
