from turtle import Turtle


class Board:
    def __init__(self):
        self.recognized = []

    def create(self, x, y, name):
        state = Turtle()
        state.hideturtle()
        state.penup()
        state.color("black")
        state.goto(x=x, y=y)
        state.write(arg=name, align="center", font=("Arial", 12, "normal"))
        self.recognized.append(name)

    def add_wrong(self, name):
        state = Turtle()
        state.hideturtle()
        state.penup()
        self.recognized.append(name)

    def completed(self):
        if len(self.recognized) == 50:
            return True

    def is_answer_on_list(self, answer):
        if answer in self.recognized:
            return True
        else:
            return False
