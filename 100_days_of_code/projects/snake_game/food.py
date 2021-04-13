from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("green")
        self.speed("fastest")
        # self.next_position()

    def next_position(self, snake):
        find_new_position = True
        x, y = 0, 0
        while find_new_position:
            x = random.randint(-200, 200)
            y = random.randint(-200, 200)
            if not any(t.distance(x, y) < 25 for t in snake.body):
                find_new_position = False

        self.goto(x, y)
