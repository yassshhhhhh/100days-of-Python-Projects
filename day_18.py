from turtle import Turtle, Screen

meow = Turtle()
meow.shape("turtle")
meow.color("cyan", "navy")
meow.speed("fast")
for _ in range(4):
    meow.forward(120)
    meow.right(90)

for _ in range(60):
    meow.forward(100)
    meow.left(122)


meow_screen = Screen()
meow_screen.exitonclick()