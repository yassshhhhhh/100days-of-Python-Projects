from turtle import Turtle, Screen
import turtle
import random

turtle.colormode(255)
meow = Turtle()
# meow.shape("turtle")
# meow.color("cyan", "navy")
meow.speed("fastest")

# for _ in range(4):
#     meow.forward(120)
#     meow.right(90)

# for _ in range(60):
#     meow.forward(100)
#     meow.left(122)

# for _ in range(15):
    # meow.pencolor("black")
    # meow.forward(10)
    # meow.pencolor("white")
    # meow.forward(10)
    # meow.forward(10)
    # meow.penup()
    # meow.forward(10)
    # meow.pendown()


# pen_colors = ["navy", "green", "black", "blue", "red", "maroon", "indigo", "olive", "brown"]


# def shape_maker(num_of_sides):
#     angle = 360/num_of_sides
#     for _ in range(num_of_sides):
#         meow.forward(100)
#         meow.left(angle)


# for sides in range(3, 11):
#     meow.pencolor(random.choice(pen_colors))
#     shape_maker(sides)


# meow.pensize(10)


# def colors():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color = (r, g, b)
#     return color


# directions = [0, 90, 180, 270]

# for _ in range(100):
#     meow.pencolor(colors())
#     meow.forward(30)
#     meow.setheading(random.choice(directions))

# def spirograph(size_of_gap):
#     for _ in range(int(360/size_of_gap)):
#         meow.color(colors())
#         meow.circle(100)
#         # meow.setheading(meow.heading() + size_of_gap)
#         meow.right(size_of_gap)


# spirograph(10)


# import colorgram
# meow.speed('fastest')

# colors = colorgram.extract('spot_painting.jpg', 30)
# colors_lst = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_tuple = (r, g, b)
#     colors_lst.append(new_tuple)
#
# print(colors_lst)

colors_list = [(234, 166, 59), (45, 112, 157), (113, 150, 203), (212, 123, 164), (16, 128, 96), (172, 44, 88), (1, 177, 143), (153, 18, 54), (224, 201, 117), (225, 76, 115), (163, 166, 35), (28, 35, 84), (227, 86, 43), (42, 166, 208), (120, 172, 116), (119, 102, 158), (215, 64, 33), (237, 244, 241), (39, 52, 100), (76, 21, 45), (229, 169, 188), (14, 99, 71), (31, 61, 56), (8, 92, 107), (222, 177, 169), (181, 188, 208), (171, 203, 193)]

meow.penup()
meow.setposition(-250, -200)
for _ in range(10):
    for _ in range(10):
        meow.dot(20, random.choice(colors_list))
        meow.penup()
        meow.forward(50)
    meow.setposition(-250, meow.pos()[1] + 50)


meow_screen = Screen()
meow_screen.exitonclick()