from os import times_result
from turtle import  Turtle,Screen
import random



tim = Turtle()
screen = Screen()
tim.teleport(-50,40)
color_pallet =["red","pink","green","blue","yellow","coral","lavender","gray"]

#
# def hexagon_movement():
#
#     tim.forward(100)
#     tim.right(60)
# def triangle_movement():
#     tim.forward(100)
#     tim.right(120)
# def square_movement():
#     tim.forward(100)
#     tim.right(90)
# def pentagon_movement():
#     tim.forward(100)
#     tim.right(72)
# def septagon_movement():
#     tim.forward(100)
#     tim.right(360/7)
# def octagon_movement():
#     tim.forward(100)
#     tim.right(360/8)
#
# def triangle():
#     for i in range(3):
#         triangle_movement()
# def square():
#     for i in range(4):
#         square_movement()
# def pentagon():
#     for i in range(5):
#         pentagon_movement()
# def hexagon():
#     for i in range(6):
#         hexagon_movement()
# def septagon():
#     for i in range(7):
#         septagon_movement()
# def octagon():
#     for i in range(8):
#         octagon_movement()
#
# tim.color(random.choice(color_pallet))
# triangle()
# tim.color(random.choice(color_pallet))
# square()
# tim.color(random.choice(color_pallet))
# pentagon()
# tim.color(random.choice(color_pallet))
# hexagon()
# tim.color(random.choice(color_pallet))
# septagon()
# tim.color(random.choice(color_pallet))
# octagon()
# screen.exitonclick()


def draw_shape(sides):
    angle = 360/sides
    tim.color(random.choice(color_pallet))
    for i in range(sides):
        tim.forward(100)
        tim.right(angle)
for side in range(3,11):
    draw_shape(side)

