import random
from turtle import Turtle, Screen


def check_listen_event():
    timmy = Turtle()
    my_screen = Screen()

    def move_forward():
        timmy.forward(100)

    my_screen.listen()
    my_screen.onkey(key="space", fun=move_forward)

    my_screen.exitonclick()


def etch_a_sketch():
    timmy = Turtle()
    my_screen = Screen()

    def move_forward():
        timmy.forward(10)

    def move_backward():
        timmy.backward(10)

    def rotate_clockwise():
        new_heading = timmy.heading() - 5
        timmy.setheading(new_heading)

    def rotate_anti_clockwise():
        timmy.left(5)

    def clear():
        timmy.clear()
        timmy.penup()
        timmy.home()
        timmy.pendown()

    my_screen.listen()
    my_screen.onkey(key="w", fun=move_forward)
    my_screen.onkey(key="s", fun=move_backward)
    my_screen.onkey(key="a", fun=rotate_anti_clockwise)
    my_screen.onkey(key="d", fun=rotate_clockwise)
    my_screen.onkey(key="c", fun=clear)

    my_screen.exitonclick()


def is_race_ended(turtles):
    resp = False
    for t in turtles:
        print(t.xcor())
        if t.xcor() >= 210:
            resp = True
            break
    return resp


def find_the_winner(turtles):
    x_coordinates = [i.xcor() for i in turtles]
    return x_coordinates.index(max(x_coordinates))


def turtle_race():

    is_race_on = False
    my_screen = Screen()
    my_screen.setup(width=500, height=400)

    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    while True:
        bet = my_screen.textinput(
            "Make you bet", "Who will win the race? Enter a colour:"
        )
        if bet in colors:
            is_race_on = True
            break
    print(f"You are betting for {bet}.")

    timmies = []
    y_start = -100
    y_diff = 30
    for c in colors:
        timmy = Turtle(shape="turtle")
        timmy.penup()
        timmy.color(c)
        timmy.goto(x=-225, y=y_start)
        y_start += y_diff
        timmies.append(timmy)

    while is_race_on:

        for t in timmies:
            d = random.randint(3, 10)
            t.forward(d)

        is_race_on = not is_race_ended(timmies)

    winner = colors[find_the_winner(timmies)]
    if winner == bet:
        print(f"You win. The winner of the race is {winner}")
    else:
        print(f"You lose. The winner of the race is {winner}")

    my_screen.exitonclick()


if __name__ == "__main__":
    # check_listen_event()
    # etch_a_sketch()
    turtle_race()
