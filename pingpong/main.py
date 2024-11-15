import time
from turtle import Screen
from ball import Ball
from paddle import Paddle
from yourScore import ScoreCard

# Set up the screen
screen = Screen()
screen.bgcolor("black")
screen.title("Pong Game")
screen.setup(width=800, height=600)
screen.tracer(0)

# Create paddles
r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
score = ScoreCard()

# Listen for keyboard input
screen.listen()
screen.onkey(l_paddle.go_down,'s')
screen.onkey(l_paddle.go_up,'w')
screen.onkey(r_paddle.go_down,'Down')
screen.onkey(r_paddle.go_up,'Up')
# Game loop
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    ball.go_cross()
    screen.update()

    # Bounce off top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()

    # Bounce off paddles
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or \
       (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_paddle()

    # Check for scoring
    if ball.xcor() > 380:
        print("Ball passed right paddle")
        score.increase_l_score()
        ball.reset_position()

    if ball.xcor() < -380:
        print("Ball passed left paddle")
        score.increase_r_score()
        ball.reset_position()

# Keep the window open
screen.exitonclick()
