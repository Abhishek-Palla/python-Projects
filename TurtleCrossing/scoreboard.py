from turtle import Turtle

FONT = ("Courier", 24, "normal")

score =0
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0  # Move `score` here as an instance variable
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 200)
        self.update_score()  # Call to display the initial score

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)

