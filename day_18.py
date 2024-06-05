from turtle import Turtle, Screen
import turtle
import random

turtle.colormode(255)
meow = Turtle()
meow.shape("turtle")
meow.color("cyan", "navy")
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


def colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


# directions = [0, 90, 180, 270]

# for _ in range(100):
#     meow.pencolor(colors())
#     meow.forward(30)
#     meow.setheading(random.choice(directions))

def spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        meow.color(colors())
        meow.circle(100)
        # meow.setheading(meow.heading() + size_of_gap)
        meow.right(size_of_gap)


spirograph(10)

meow_screen = Screen()
meow_screen.exitonclick()