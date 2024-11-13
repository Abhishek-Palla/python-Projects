# snake.py

from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:

    def __init__(self):
        self.segments = []
        self.direction = "right"  # Default direction
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            segment = Turtle("square")
            segment.color('white')
            segment.penup()
            segment.goto(position)
            self.segments.append(segment)

    def add_segment(self):
        # Add a new segment at the last segment’s position
        new_segment = Turtle("square")
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(self.segments[-1].position())
        self.segments.append(new_segment)

    def move(self):
        # Move the snake body segments in reverse order
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        # Set the head direction based on current direction
        if self.direction == 'up':
            self.segments[0].setheading(90)
        elif self.direction == 'down':
            self.segments[0].setheading(270)
        elif self.direction == 'left':
            self.segments[0].setheading(180)
        elif self.direction == 'right':
            self.segments[0].setheading(0)

        self.segments[0].forward(MOVE_DISTANCE)
