from box import Box
import random
from turtle import Vec2D
from player import Player

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self, screen_width:int, screen_height: int) -> None:
        self.car_list=[]
        self.screen_height= screen_height
        self.screen_width= screen_width
        self.level=1
        self.car_list.append(Car(self.level, screen_width, screen_height))
        self.max_cars=self.level*3+10
    
    def if_max_cars(self):
        if len(self.car_list)>=self.max_cars:
            return True
        return False

    def add_car(self):
        self.car_list.append(Car(self.level, self.screen_width, self.screen_height))
    
    def move(self):
        for car in self.car_list:
            car.move()
            if car.position()[0]<=-self.screen_width:
                self.car_list.remove(car)

    def level_up(self):
        self.level += 1
        self.max_cars = self.level*3 +10
        self.car_list.clear()
        self.car_list.append(Car(self.level, self.screen_width, self.screen_height))
    
    def is_Accident(self, turtle: Player):
        for car in self.car_list:
            if car.detect_collision(turtle):
                return True
        return False


class Car(Box):
    def __init__(self, level: int, screen_width:int, screen_height: int, undobuffersize: int = 1000, visible: bool = True, width: int = 20, height: int = 20) -> None:
        super().__init__(undobuffersize, visible, (screen_width//2, random.randint(-screen_height//2, screen_height//2)) , width, height)
        self.color(random.choice(COLORS))
        self.velocity= Vec2D(-STARTING_MOVE_DISTANCE*level, 0)    
     
