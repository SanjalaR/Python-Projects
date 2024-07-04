from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__('circle')
        self.color('white')
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.speed = 0.1

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def speed_up(self):
        self.speed *= 0.9
        print(f'Speed is {self.speed}')
