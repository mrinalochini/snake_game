import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.listen()

snake = Snake()
snack = Food()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
mark = Scoreboard()

to_continue = True
while to_continue:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision with food
    if snake.head.distance(snack) < 15:
        snack.refresh()
        snake.extend()
        mark.sum()

    #Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        to_continue = False
        mark.game_over()

    #Detect collisions with tail.
    for segment in snake.body[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            mark.game_over()

screen.exitonclick()