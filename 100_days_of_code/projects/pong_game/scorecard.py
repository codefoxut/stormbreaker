from turtle import Turtle

CENTER_ALIGNMENT = "center"
FONT = ("courier", 80, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.left = 0
        self.right = 0
        self.display_the_score()

    def display_the_score(self):

        self.goto(-100, 200)
        self.write(self.left, align=CENTER_ALIGNMENT, font=FONT)

        self.goto(100, 200)
        self.write(self.right, align=CENTER_ALIGNMENT, font=FONT)

    def point_to_left(self):
        self.left += 1
        self.clear()
        self.display_the_score()

    def point_to_right(self):
        self.right += 1
        self.clear()
        self.display_the_score()
