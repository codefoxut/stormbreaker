from turtle import Turtle, Screen

from prettytable import PrettyTable


def check_turtle():
    tonu = Turtle()
    print(tonu)
    tonu.shape("turtle")
    tonu.color("coral")

    my_screen = Screen()
    print(my_screen.screensize())
    print(tonu.position())
    tonu.forward(100.0)
    print(tonu.position())
    my_screen.exitonclick()


def check_pretty_table():
    pt = PrettyTable()
    pt.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
    pt.add_column("Type", ["Electric", "Water", "Fire"])
    pt.align = "r"
    print(pt)


if __name__ == "__main__":
    # check_turtle()
    check_pretty_table()
