import time
import schedule
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

SPEED = 0.1

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

turtle = Player()
board = Scoreboard()
cars = []

screen.onkey(key= "Up", fun= turtle.move)

def auto_gen_car():
    car = CarManager()
    cars.append(car)


schedule.every(2).seconds.do(auto_gen_car)
game_is_on = True
while game_is_on:
    time.sleep(SPEED)
    screen.update()
    schedule.run_pending()

    for i in range(len(cars)):
        cars[i].running()
        if turtle.distance(cars[i]) < 30:
            game_is_on = False
            board.game_over()   

    if turtle.win():
        board.upgrade()
        if SPEED > 0:
            SPEED -= 0.01


screen.exitonclick()
