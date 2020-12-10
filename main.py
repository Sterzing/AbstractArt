
# import colorgram
# colors = colorgram.extract("OonTracks.jpg", 20)
#
#
# def tuple_it(color_object):
#     red = color_object[0]
#     green = color_object[1]
#     blue = color_object[2]
#     return (red, green, blue)
#
#
# rgb_list = []
# for color in range(len(colors)):
#     next_color = colors[color].rgb
#     rgb = tuple_it(next_color)
#     rgb_list.append(rgb)
# print(rgb_list)
from turtle import Turtle, Screen
import random
t = Turtle()
screen = Screen()
screen.colormode(255)

color_list = [(178, 158, 127), (115, 95, 80), (30, 35, 56), (203, 226, 239), (242, 239, 231), (143, 139, 93),
              (54, 58, 80), (160, 172, 180), (227, 236, 234), (72, 76, 97), (164, 174, 169), (207, 199, 149),
              (69, 51, 43), (166, 113, 96), (159, 153, 155), (229, 176, 164), (109, 95, 100), (235, 229, 231),
              (88, 54, 45), (176, 197, 203)]


t.penup()
t.hideturtle()
t.speed("fastest")
# t.goto(-235, -150)


def horizontal(up):
    right = -230
    for _ in range(10):
        t.goto(right, up)
        t.dot(20, random.choice(color_list))
        right += 50


go_up = -225
for _ in range(10):
    horizontal(go_up)
    go_up += 50




screen.exitonclick()
