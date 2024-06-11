from turtle import Screen, Turtle

# from animal import Animal
# from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Animal(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.setheading(90)
        self.penup()
        self.go_to_start()

    def move_forward(self):
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        if self.ycor() >= FINISH_LINE_Y:
            return True
        else:
            return False


# from cars import Cars
# from turtle import Turtle
import random
COLORS = ["red", "yellow", "orange", "Blue", "green", "brown", "purple"]
STARING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Cars:

    def __init__(self):
        self.all_cars = []
        self.move_distance = STARING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.move_distance)

    def level_up(self):
        self.move_distance += MOVE_INCREMENT


# from scoreboard import Scoreboard
# from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(-280, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.write("Game over!", align="center", font=FONT)


import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Cross the Turtle")
screen.bgcolor("black")
screen.tracer(0)

animal = Animal()
cars = Cars()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(animal.move_forward, "Up")

is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()

    cars.create_car()
    cars.move_cars()

    # Detecting collision with car
    for car in cars.all_cars:
        if car.distance(animal) < 20:
            is_game_on = False
            scoreboard.game_over()

    # Detecting successful crossing
    if animal.is_at_finish_line():
        animal.go_to_start()
        cars.level_up()
        scoreboard.update_scoreboard()


screen.exitonclick()
