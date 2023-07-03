start_pos = [(0, 0), (-20, 0), (-40, 0)]
from turtle import Turtle

mup = 90
mdown = 270
mright = 0
mleft = 180

move_dist = 20


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def add_seg(self, turtle_i):
        tim = Turtle()
        tim.penup()
        tim.shape("square")
        tim.color("white")
        tim.goto(turtle_i)
        self.segments.append(tim)

    def create_snake(self):
        for turtle_i in start_pos:
            self.add_seg(turtle_i)




    def extend(self):
        self.add_seg(self.segments[-1].position())
    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            x = self.segments[i - 1].xcor()
            y = self.segments[i - 1].ycor()
            self.segments[i].goto(x, y)
        self.head.forward(move_dist)

    def up(self):
        if self.head.heading() != mdown:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != mup:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != mleft:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != mright:
            self.head.setheading(180)




