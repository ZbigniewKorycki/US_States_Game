from turtle import Turtle

MAX_SCORE = 50


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.create()

    def create(self):
        self.hideturtle()
        self.penup()
        self.goto(250, 250)

    def update(self):
        self.score += 1

    def finish(self):
        self.clear()
        self.goto(0, 0)
        self.write(arg="GAME OVER", align="center", font=("Arial", 100, "normal"))

    def time_is_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(arg="TIME IS OVER", align="center", font=("Arial", 100, "normal"))

    def get_score(self):
        return self.score

    def get_max_score(self):
        return MAX_SCORE
