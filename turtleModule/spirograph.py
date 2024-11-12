import turtle
import random

t = turtle.Turtle()
screen = turtle.Screen()

t.speed("fastest")
screen.colormode(255)

def random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    return (r, g, b)

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        t.pencolor((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        t.circle(100)
        t.setheading(t.heading() + size_of_gap)



draw_spirograph(5)
screen.exitonclick()