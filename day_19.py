from turtle import Turtle, Screen

meow = Turtle()

def move_forward():
    meow.forward(20)

def move_backward():
    meow.backward(20)

def move_count_clockwise():
    meow.left(20)

def move_clockwise():
    meow.right(20)

def clear():
    meow.reset()


screen = Screen()
screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(move_count_clockwise, "a")
screen.onkey(move_clockwise, "d")
screen.onkey(clear, "c")
screen.exitonclick()