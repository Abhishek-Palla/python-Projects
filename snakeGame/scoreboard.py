# scoreboard.py

from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 220)  # Position the scoreboard at the top center of the screen
        self.update_score()

    def update_score(self):
        self.clear()  # Clear the previous score
        self.write(f"Score: {self.score}", align="center", font=("Arial", 16, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 24, "bold"))
