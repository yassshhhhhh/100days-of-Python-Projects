# Pong Game
from turtle import Screen
# from paddle import Paddle

from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def move_up(self):
        new_y = self.ycor() + 40
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 40
        self.goto(self.xcor(), new_y)



# from ball import Ball

from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()


# from scoreboard import Scoreboard

from turtle import Turtle
FONT_1 = ("courier", 50, "normal")
FONT_2 = ("courier", 30, "normal")
FONT_3 = ("courier", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.right_score = 0
        self.left_score = 0
        self.score_to_win = 10
        self.color("white")
        self.hideturtle()
        self.penup()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(100, 200)
        self.write(arg=self.right_score, align="center", font=FONT_1)
        self.goto(-100, 200)
        self.write(arg=f"{self.left_score}", align="center", font=FONT_1)

    def add_score_to_right_paddle(self):
        self.right_score += 1
        self.update_score()

    def add_score_to_left_paddle(self):
        self.left_score += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="Game Over!", align="center", font=FONT_2)

    def left_wins(self):
        self.goto(0, -30)
        self.write(arg="Left Wins.", align="center", font=FONT_3)

    def right_wins(self):
        self.goto(0, -30)
        self.write(arg="Right Wins.", align="center", font=FONT_3)


import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong-Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    # print(ball.pos())

    # Detecting the ball collision with wall and bounce
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    # detecting the ball collision with paddle and bounce
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detecting if ball misses right paddle
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.add_score_to_left_paddle()
        if scoreboard.left_score == scoreboard.score_to_win:
            scoreboard.game_over()
            scoreboard.left_wins()
            is_game_on = False

    # Detecting if ball misses left paddle
    if ball.xcor() < -380:
        ball.reset()
        scoreboard.add_score_to_right_paddle()
        if scoreboard.right_score == scoreboard.score_to_win:
            scoreboard.game_over()
            scoreboard.right_wins()
            is_game_on = False


screen.exitonclick()

