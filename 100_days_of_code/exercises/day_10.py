import random
from turtle import Turtle, Screen, colormode
from tkinter import *


def check_turtle():
    timmy = Turtle()
    timmy.shape("turtle")
    timmy.color("cyan", "green")
    timmy.forward(100)

    screen = Screen()
    screen.exitonclick()


def draw_square():
    timmy = Turtle()
    timmy.shape("turtle")
    for _ in range(4):
        timmy.forward(100)
        timmy.left(90)

    screen = Screen()
    screen.exitonclick()


def draw_dashed_line():
    timmy = Turtle()
    timmy.shape("turtle")
    for _ in range(20):
        timmy.forward(10)
        if timmy.isdown():
            timmy.penup()
        else:
            timmy.pendown()

    screen = Screen()
    screen.exitonclick()


def draw_all_shape():
    timmy = Turtle()
    timmy.shape("triangle")
    for i in range(3, 11):
        r = random.randint(1, 255) / 255
        g = random.randint(1, 255) / 255
        b = random.randint(1, 255) / 255
        timmy.color(r, g, b)
        print(timmy.color())
        angle = 360 / i
        for j in range(i):
            timmy.forward(100)
            timmy.right(angle)

    screen = Screen()
    screen.exitonclick()


def draw_random_walk():
    timmy = Turtle()
    timmy.shape("triangle")
    timmy.pensize(15)
    timmy.speed("fastest")
    colormode(255)
    for _ in range(500):
        r = random.randint(1, 255)
        g = random.randint(1, 255)
        b = random.randint(1, 255)
        timmy.color(r, g, b)
        angle = random.choice([0, 90, 180, 270])
        timmy.setheading(angle)
        timmy.forward(25)

    screen = Screen()
    screen.exitonclick()


def random_color():
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    return r, g, b


def draw_spirograph():
    timmy = Turtle()
    timmy.shape("classic")
    # timmy.pensize(15)
    timmy.speed("fastest")
    colormode(255)
    tilt_angle = random.randint(5, 15)

    for i in range(2 * 360 // tilt_angle):
        timmy.color(random_color())
        timmy.setheading(tilt_angle * i)
        timmy.circle(40)
        timmy.forward(40)

    screen = Screen()
    screen.exitonclick()


def choose_colors():
    import colorgram
    colors = colorgram.extract("damien.jpeg", 50)
    return colors


def draw_hirst():
    colors = choose_colors()
    timmy = Turtle()
    timmy.shape("classic")
    # timmy.pensize(15)
    timmy.speed("fastest")
    colormode(255)

    for x in range(-250, 250, 40):
        for y in range(-250, 250, 40):
            color = random.choice(colors)
            timmy.penup()
            timmy.goto(y, x)
            timmy.pendown()
            timmy.dot(20, color.rgb)

    screen = Screen()
    screen.exitonclick()


if __name__ == '__main__':
    # check_turtle()
    # draw_square()
    # draw_dashed_line()
    # draw_all_shape()
    # draw_random_walk()
    # draw_spirograph()
    # choose_colors()
    draw_hirst()
