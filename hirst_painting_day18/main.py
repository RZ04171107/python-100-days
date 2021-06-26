# import colorgram
#
# NUM_OF_COLORS = 30
# colors = colorgram.extract('hirst_painting.jpg', NUM_OF_COLORS)
#
# rgb_colors = []
#
# def get_rgb_tuple(color_index):
#     r = colors[color_index].rgb.r
#     g = colors[color_index].rgb.g
#     b = colors[color_index].rgb.b
#     return tuple((r, g, b))
#
# for _index in range(NUM_OF_COLORS):
#     rgb_colors.append(get_rgb_tuple(_index))
#
# print(rgb_colors)

list_colors = [(239, 230, 246), (218, 237, 246), (20, 111, 171), (187, 16, 63), (231, 145, 77), (243, 219, 84), (169, 45, 104), (227, 125, 158), (40, 51, 119), (227, 56, 107), (116, 169, 208), (63, 169, 80), (229, 77, 60), (124, 190, 147), (131, 77, 48), (18, 138, 64), (10, 173, 205), (209, 155, 11), (19, 50, 94), (252, 228, 0), (24, 96, 46), (151, 209, 220), (116, 43, 35), (69, 75, 40), (239, 162, 185), (153, 210, 195), (7, 77, 51), (237, 169, 158)]

from turtle import Turtle, Screen
import random

screen = Screen()
screen.colormode(255)
timmy = Turtle()

#set the beginning position
START_X = -250
START_Y = -250
SPACE = 50

timmy.speed("fastest")
timmy.penup()
timmy.goto(START_X, START_Y)

#def pick_random_color_from_list():

def draw_a_row():
    for _ in range(10):
        timmy.pencolor(random.choice(list_colors))
        timmy.dot(20)
        timmy.penup()
        timmy.forward(SPACE)

    timmy.penup()
    timmy.goto(START_X, timmy.ycor() + SPACE)


for _ in range(10):
    draw_a_row()

screen.exitonclick()
