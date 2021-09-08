import turtle
import time
from snake import Snake
from food import Food
from scoreboard import Score
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('SNAKE GAME')

screen.tracer(0)
snake = Snake()
food = Food()
score = Score()
game_on = True
screen.update()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.right, 'Right')
screen.onkey(snake.left, 'Left')


while game_on:
    screen.update()
    snake.move()
    time.sleep(0.2)

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.expand_snake()
        score.update_score()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        score.game_over()

    for i in range(1, len(snake.snake)):
        if snake.head.distance(snake.snake[i]) < 10:
            game_on = False
            score.game_over()


screen.exitonclick()
