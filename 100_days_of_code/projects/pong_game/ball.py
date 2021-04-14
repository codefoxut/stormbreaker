import random
from turtle import Turtle

COLORS = ["blue", "orange", "red", "green", "white", "purple", "yellow"]
MOVING_TOWARDS = ["left", "right"]


class Ball(Turtle):
    def __init__(self):
        super().__init__(shape="circle")
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.penup()
        self.moving_to = ""
        self.color("green")
        self.speed("fastest")
        move_to = random.choice(MOVING_TOWARDS)
        move_func = getattr(self, f"move_towards_{move_to}")
        move_func()
        self.move_speed = 0.1

    def move_towards_right(self):
        self.moving_to = "right"
        angles = list(range(0, 90)) + list(range(271, 360))
        self.setheading(random.choice(angles))

    def move_towards_left(self):
        self.moving_to = "left"
        angles = list(range(91, 270))
        self.setheading(random.choice(angles))

    def move(self):
        self.forward(20)

    def touching_the_wall(self):
        return self.ycor() > 280 or self.ycor() < -270

    def bounce_from_wall(self):
        self.setheading(360 - self.heading())

    def bounce_from_paddle(self):
        self.moving_to = "right" if self.moving_to == "left" else "left"
        heading = self.heading()
        if heading < 90 or heading > 270:
            heading = heading - 360 if heading > 270 else heading
            self.setheading(180 - heading)
        else:
            heading = (180 - heading) % 360
            self.setheading(heading)
        self.move_speed *= 0.95
        print("bounce", self.heading())

    def reset_position(self):

        if self.moving_to == "right":
            self.move_towards_left()
        else:
            self.move_towards_right()
        self.goto(0, 0)
        # self.bounce_from_paddle()
        self.color(random.choice(COLORS))
        self.move_speed = 0.1
