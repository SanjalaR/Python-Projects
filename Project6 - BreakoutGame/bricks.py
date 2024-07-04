import turtle
from turtle import Turtle
import random

COLORS = [(58,166,185), (255, 158, 170), (255, 208, 208), (249, 249, 224)]

class Brick(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.penup()
        self.shape('square')
        self.shapesize(stretch_wid=2, stretch_len=3)
        turtle.colormode(255)
        self.color(random.choice(COLORS))
        self.goto(x, y)

        self.left_wall = self.xcor() - 30
        self.right_wall = self.xcor() + 30
        self.upper_wall = self.ycor() + 15
        self.bottom_wall = self.ycor() - 15

class Bricks:
    def __init__(self):
        self.list = []
        self.x = -365
        self.y = 250
        self.shift = 0
        self.populate()

    def populate(self):
        for i in range(33):
            new_brick = Brick(self.x, self.y)
            self.list.append(new_brick)
            self.x += 65
            if self.x >= (380 - self.shift):
                self.x = -380
                self.shift += 30
                self.x += self.shift
                self.y -= 50

    def disappear(self, i):
        # i.color('black')
        i.clear()
        i.goto(3000,3000)
        self.list.remove(i)
