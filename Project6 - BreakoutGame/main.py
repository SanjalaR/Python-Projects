import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from bricks import Bricks
from scoreboard import ScoreBoard

MILESTONES = [4, 20, 40, 60, 80, 100, 120]
screen = Screen()
screen.setup(800, 600)
screen.bgcolor('black')
screen.title('Breakout')
screen.tracer(0)

paddle = Paddle((0, -280))
screen.listen()
screen.onkey(fun=paddle.left, key='Left')
screen.onkey(fun=paddle.right, key='Right')

ball = Ball()
bricks = Bricks()
sb = ScoreBoard()


game = True
while game:
    time.sleep(ball.speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.distance(paddle) < 30:
        ball.bounce_y()

    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()

    if ball.ycor() < -290:
        sb.update_minus()
        ball.goto(0, 0)
        ball.bounce_x()
        ball.speed = 0.1

    for i in bricks.list:
        if ball.distance(i) < 40:
            sb.update_plus()
            if sb.score in MILESTONES:
                ball.speed_up()
            bricks.disappear(i)
            if ball.xcor() < i.left_wall or ball.xcor() > i.right_wall:
                ball.bounce_x()
            elif ball.ycor() < i.bottom_wall or ball.ycor() > i.upper_wall:
                ball.bounce_y()

    if sb.lives == 0:
        game = False
        sb.lost()

    if len(bricks.list) == 0:
        game = False
        sb.won()

screen.exitonclick()
