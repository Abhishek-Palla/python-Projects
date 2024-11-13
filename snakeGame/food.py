# food.py

from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        # Explicitly initialize the Turtle instance
        Turtle.__init__(self)
        self.shape("circle")
        self.color("red")
        self.penup()
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        # Move the food to a new random position
        x_position = random.randint(-230, 230)
        y_position = random.randint(-230, 230)
        self.goto(x_position, y_position)
