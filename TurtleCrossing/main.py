import time
from turtle import Screen
from player import Player, STARTING_POSITION
from car_manager import CarManager
import random
from scoreboard import Scoreboard

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

# Player setup
player = Player()
screen.onkey(player.move_straight, 'w')
screen.onkey(player.move_back, 's')

# Car manager setup
car_manager = CarManager()

# Scoreboard setup
score = Scoreboard()

# Game variables
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Create new cars periodically
    if random.randint(1, 6) == 1:  # Adjust frequency
        car_manager.create_car()

    # Move all cars
    car_manager.move_cars()

    # Collision detection
    for car in car_manager.all_cars:
        if car.distance(player) < 20:  # Collision detected
            game_is_on = False
            score.game_over()

    # Check if player wins
    if player.ycor() > 280:  # Finish line
        player.goto(STARTING_POSITION)
        car_manager.increase_speed()  # Cars move faster on each level
        score.increase_score()
