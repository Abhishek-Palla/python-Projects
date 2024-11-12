from turtle import Turtle,Screen
import random


direction =[0,90,180,270]

tim  = Turtle()
screen  = Screen()
screen.colormode(255)


tim.width(10)
for i in range(100):
    tim.pencolor((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    tim.forward(25)
    tim.setheading(random.choice(direction))
screen.exitonclick()

