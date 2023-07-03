import time
from turtle import Screen
from snake import Snake
from food import Food
from scorebd import Board

scrn = Screen()
scrn.setup(width=600, height=600)
scrn.bgcolor("black")
scrn.title("Snake")
scrn.tracer(0)
snake = Snake()
food = Food()
scorebd = Board()
scrn.listen()
scrn.onkey(snake.up, "Up")
scrn.onkey(snake.down, "Down")
scrn.onkey(snake.left, "Left")
scrn.onkey(snake.right, 'Right')
is_game = True
while is_game:
    scrn.update()
    time.sleep(0.5)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scorebd.increase()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scorebd.game_over()
        is_game = False
    for segment in snake.segments[1:]:
       if snake.head.distance(segment)<10:
            is_game = False
            scorebd.game_over()

scrn.exitonclick()
