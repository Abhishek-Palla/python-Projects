from turtle import Turtle,Screen
import random

turtle_colors = [
    "red", "blue", "green", "yellow", "orange", "purple",
    "pink", "brown", "black", "gray", "cyan",
    "magenta", "lime", "navy", "aqua", "teal", "maroon",
    "olive", "silver", "turquoise", "violet", "gold", "indigo",
    "coral", "salmon", "khaki", "plum", "orchid", "tan",
    "skyblue", "peru", "crimson", "tomato", "sienna", "chocolate",
    "firebrick", "forestgreen", "limegreen", "seagreen", "darkgreen",
    "darkorange", "darkviolet", "deeppink", "deepskyblue", "dodgerblue",
    "hotpink", "indianred", "lavender", "lightblue"
]
direction =[0,90,180,270]

tim  = Turtle()
screen  = Screen()
movement =["forward","backward"]

tim.width(10)
for i in range(100):
    tim.color(random.choice(turtle_colors))
    tim.forward(25)
    tim.setheading(random.choice(direction))
screen.exitonclick()

