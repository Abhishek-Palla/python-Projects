# main.py

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Set up the screen
screen = Screen()
screen.setup(500, 500)
screen.bgcolor("black")
screen.title("Simple Snake Game")
screen.tracer(0)  # Turn off automatic updates
screen.listen()

# Create the snake, food, and scoreboard
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Direction control functions
def go_up():
    if snake.direction != 'down':
        snake.direction = 'up'

def go_down():
    if snake.direction != 'up':
        snake.direction = 'down'

def go_left():
    if snake.direction != 'right':
        snake.direction = 'left'

def go_right():
    if snake.direction != 'left':
        snake.direction = 'right'

# Set up key listeners
screen.onkey(go_up, "w")
screen.onkey(go_down, "s")
screen.onkey(go_left, "a")
screen.onkey(go_right, "d")

# Main game loop
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Check for collision with food
    if snake.segments[0].distance(food) < 15:
        food.refresh()  # Move the food to a new random location
        snake.add_segment()  # Grow the snake
        scoreboard.increase_score()  # Update the score

    # Check for wall collision
    if (snake.segments[0].xcor() > 240 or snake.segments[0].xcor() < -240 or
        snake.segments[0].ycor() > 240 or snake.segments[0].ycor() < -240):
        game_on = False
        scoreboard.game_over()  # Display game over message

screen.exitonclick()
