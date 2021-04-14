from turtle import Turtle

PADDLE_SIZE = 5
BLOCK_SIZE = 20

UP = 90
DOWN = 270


class Paddle(Turtle):
    def __init__(self, x_pos):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(x_pos, 0)

    def up(self):
        if self.ycor() < 230:
            y_pos = self.ycor() + 20
            self.goto(self.xcor(), y_pos)

    def down(self):
        if self.ycor() > -220:
            y_pos = self.ycor() - 20
            self.goto(self.xcor(), y_pos)
