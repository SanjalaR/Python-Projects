from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.penup()
        self.goto(0, 280)
        self.score = -4
        self.lives = 3
        self.update_plus()

    def update_plus(self):
        self.clear()
        self.score += 4
        self.write(arg=f'Score: {self.score}    Lives: {self.lives}', move=False, align="center", font=("Courier", 14, "normal"))


    def update_minus(self):
        self.clear()
        self.lives-=1
        self.write(arg=f'Score: {self.score}    Lives: {self.lives}', move=False, align="center", font=("Courier", 14, "normal"))

    def lost(self):
        self.goto(0, 0)
        self.write("You lost!", move=False, align="center", font=("Courier", 14, "normal"))

    def won(self):
        self.goto(0, 0)
        self.write("You won!", move=False, align="center", font=("Courier", 14, "normal"))
