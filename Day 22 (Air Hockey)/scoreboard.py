from turtle import Turtle

class ScoreCard(Turtle):
    def __init__(self, position: tuple, shape: str = "classic", undobuffersize: int = 1000, visible: bool = False) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.setposition(position)
        
    def print_score(self, score: int):
        self.clear()
        self.pencolor('white')
        self.pendown()
        self.write(score)
        


