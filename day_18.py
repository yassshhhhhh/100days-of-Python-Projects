from turtle import Turtle, Screen
import random

meow = Turtle()
meow.shape("turtle")
meow.color("cyan", "navy")
meow.speed("fast")

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


pen_colors = ["navy", "green", "black", "blue", "red", "maroon", "indigo", "olive", "brown"]


def shape_maker(num_of_sides):
    angle = 360/num_of_sides
    for _ in range(num_of_sides):
        meow.forward(100)
        meow.left(angle)


for sides in range(3, 11):
    meow.pencolor(random.choice(pen_colors))
    shape_maker(sides)


meow_screen = Screen()
meow_screen.exitonclick()