import snake
import food
from turtle import Turtle

align = "center"
FONT = ('Arial', 24, 'normal')


class Board(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0

        self.color("white")
        self.penup()
        self.ht()
        self.goto(0, 270)

        self.write(f"Score :{self.score}", align=align, font=FONT)


    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over", align=align, font=FONT)
    def increase(self):
        self.score += 1
        self.clear()
        self.write(f"Score :{self.score}", align=align, font=FONT)


