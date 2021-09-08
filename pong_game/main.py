import turtle
import time
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('PONG GAME')

screen.tracer(0)

game_on = True


r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
scoreboard = ScoreBoard()
ball = Ball(800, 600)
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, 'Down')
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, 's')

screen.listen()
sleep = 0.1
while game_on:

    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    if (ball.distance(r_paddle) <= 50 and ball.xcor() >= 340) or (ball.distance(l_paddle) <= 50 and ball.xcor() <= -340):
        ball.x_bounce()

    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.new_round()
        if sleep >= 0.02:
            sleep -= 0.02

    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.new_round()
        if sleep >= 0.02:
            sleep -= 0.02
    print(sleep)
    time.sleep(sleep)


screen.exitonclick()
