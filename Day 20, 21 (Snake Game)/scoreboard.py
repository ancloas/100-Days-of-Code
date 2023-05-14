from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = False) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.score = 0
        with open('Day 20, 21 (Snake Game)\data.txt') as data:
            self.high_score=int(data.read())
        self.color('white')
        self.color('yellow')
        self.penup()
        self.setposition(0,280)
        self.pendown()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f'Score: {self.score} High Score: {self.high_score}')
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score=self.score
            with open('Day 20, 21 (Snake Game)\data.txt', mode='w') as highscore:
                highscore.write(str(self.high_score))
        self.score=0
        self.update_scoreboard()
    
    def increase_score(self):
        self.score+=1
        self.update_scoreboard()