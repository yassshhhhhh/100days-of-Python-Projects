# Guess the states in US.
import turtle
import pandas
# from states import States
from turtle import Turtle


class States(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")

    def update_state(self, state_name):
        self.write(state_name)

    def update_position(self, x, y):
        self.goto(x, y)



screen = turtle.Screen()
screen.title("U.S. State Games")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data["state"]
x_axis = data["x"]
y_axis = data["y"]

correct_states = 0
answer_state = screen.textinput(title="Guess the state", prompt="Enter the state name?").lower()
oop_states = States()
list_of_states = states.to_list()
answered_states = []


while True:

    if answer_state == "exit":
        remaining_states = [] #remaining_states = [state for state in list_of_states if state not in answered_states]
        for state in list_of_states:
            if state not in answered_states:
                remaining_states.append(state)
        new_data = pandas.DataFrame(remaining_states)
        new_data.to_csv("states_to_learn.csv")
        break

    for state in range(len(states)):
        if states[state].lower() == answer_state:
            answered_states.append(states[state])
            oop_states.update_position(x_axis[state], y_axis[state])
            oop_states.update_state(states[state])
            correct_states += 1

    answer_state = screen.textinput(title=f"{correct_states}/50 States Correct", prompt="What's another state name?").lower()

# def get_mouse_click_coordinates(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coordinates)
# turtle.mainloop()
# screen.exitonclick()
