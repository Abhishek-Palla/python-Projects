from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shapesize(1,1)
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_pos = 0
        self.y_pos = 0
        self.x_move = 10
        self.y_move = 10

    def go_cross(self):
        self.x_pos += self.x_move
        self.y_pos += self.y_move
        self.goto(self.x_pos, self.y_pos)

    def bounce_wall(self):
        self.y_move *= -1

    def bounce_paddle(self):
        self.x_move *= -1

    def reset_position(self):
        self.x_pos = 0
        self.y_pos = 0
        self.goto(self.x_pos, self.y_pos)
