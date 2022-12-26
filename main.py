from turtle import Screen, Turtle
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
food = Food()
scoreboard = Scoreboard()

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 15:
        scoreboard.change_score(scoreboard.score + 1)
        snake.extend()
        food.refresh()

    # Detect collision with the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        snake.reset()
        scoreboard.reset()

    # Detect collision with the tail
    for i in range(1, len(snake.segments)):
        if snake.head.distance(snake.segments[i]) < 10:
            snake.reset()
            scoreboard.reset()
            break




screen.exitonclick()
