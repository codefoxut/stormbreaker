from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    block_size = 20
    initial_size = 3

    def __init__(self):
        self.body = []
        self.create_body()
        self.head = self.body[0]

    def add_segment(self, position):
        t = Turtle(shape="square")
        t.penup()
        t.color("white")
        t.goto(position)
        self.body.append(t)

    def create_body(self):
        x = 0
        for i in range(self.initial_size):
            position = (x, 0)
            self.add_segment(position)
            # t.speed(3 + 3 * i)
            x -= self.block_size

    def change_the_direction(self, direction="forward"):
        heading = self.body[0].heading()
        if direction == "anticlockwise":
            self.head.setheading(heading + 90)
        elif direction == "clockwise":
            self.head.setheading(heading - 90)

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].setheading(self.body[i - 1].heading())
            self.body[i].goto(self.body[i - 1].pos())
        self.head.forward(self.block_size)

    # def move_forward(self):
    #     self.move_snake(direction='forward')
    #
    def move_anticlockwise(self):
        self.change_the_direction(direction="anticlockwise")

    def move_clockwise(self):
        self.change_the_direction(direction="clockwise")

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def extend(self):
        self.add_segment(self.body[-1].pos())
        print(len(self.body))

    def hit_the_wall(self):
        return (
            self.head.xcor() > 290
            or self.head.xcor() < -290
            or self.head.ycor() > 290
            or self.head.ycor() < -290
        )

    def hit_the_tail(self):
        resp = False
        for i in range(1, len(self.body)):
            if self.head.distance(self.body[i]) < 15:
                resp = True
                break
        return resp
