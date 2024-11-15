from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color('white')
        self.goto(STARTING_POSITION)
        self.left(90)  # Turn the turtle to face upwards
        self.shapesize(stretch_wid=1, stretch_len=2)  # Remove this line


    def move_straight(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def move_back(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_y)
