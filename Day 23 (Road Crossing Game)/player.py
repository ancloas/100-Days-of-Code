from box import Box

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Box):
    def __init__(self,position: tuple, undobuffersize: int = 1000, visible: bool = True, width: int = 20, height: int = 20) -> None:
        super().__init__(undobuffersize, visible, position, width, height)
        self.setposition(position)
        self.color('green')

    def move(self):
        self.setpos(self.position()[0], self.position()[1]+MOVE_DISTANCE)
    
    def is_Reached_Finish(self, finish_line):
        if self.position()[1]>=finish_line:
            return True
        
    def is_Accident(self, cars: Box):
        if self.detect_collision(cars):
            return True
        return False