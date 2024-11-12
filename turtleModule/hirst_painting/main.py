# import colorgram
from turtle import Turtle,Screen
import random


# colors_list =[]
# colors = colorgram.extract('hirst.jpg', 6)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     colors_list.append(new_color)
# print(colors_list)

my_project_colors =[(225, 224, 209), (0, 0, 0), (164, 88, 39), (111, 35, 63), (2, 113, 179), (220, 177, 8)]
tim = Turtle()
S = Screen()

S.colormode(255)

start_x = -225
start_y = 225

for i in range(10):
    tim.penup()
    tim.goto(start_x, start_y - i * 50)

    for j in range(10):
        tim.dot(20, random.choice(my_project_colors))
        tim.forward(50)

S.exitonclick()







