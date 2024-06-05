# from turtle import Turtle, Screen

# # meow = Turtle()

# # def move_forward():
# #     meow.forward(20)

# # def move_backward():
# #     meow.backward(20)

# # def move_count_clockwise():
# #     meow.left(20)

# # def move_clockwise():
# #     meow.right(20)

# # def clear():
# #     meow.reset()

# # screen = Screen()
# # screen.listen()
# # screen.onkey(move_forward, "w")
# # screen.onkey(move_backward, "s")
# # screen.onkey(move_count_clockwise, "a")
# # screen.onkey(move_clockwise, "d")
# # screen.onkey(clear, "c")

# screen.exitonclick()


from turtle import Turtle, Screen
import random

is_game_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which color turtle will win the race? Enter a choice: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
y_positions = [-100, -60, -20, 20, 60, 100]

for turtle_index in range(len(colors)):
    new_turtle = Turtle("turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_game_on = True

while is_game_on:
    for turtle in all_turtles:
        if turtle.xcor() > 220:
            is_game_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()

